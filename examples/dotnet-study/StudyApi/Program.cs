using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);
var path = builder.Configuration["DatabasePath"] ?? "study.db";
var fullPath = Path.GetFullPath(path);
Directory.CreateDirectory(Path.GetDirectoryName(fullPath)!);

builder.Services.AddProblemDetails();
builder.Services.AddDbContext<StudyDb>(options =>
    options.UseSqlite($"Data Source={fullPath}"));

var app = builder.Build();
app.UseExceptionHandler();

if (args.Contains("--migrate"))
{
    using var scope = app.Services.CreateScope();
    var db = scope.ServiceProvider.GetRequiredService<StudyDb>();
    await db.Database.MigrateAsync();
    return;
}

app.MapGet("/health", () => Results.Ok(new { status = "ok" }));

app.MapGet("/api/jobs", async (StudyDb db, CancellationToken ct) =>
{
    var rows = await db.Jobs.AsNoTracking()
        .OrderBy(x => x.Id)
        .Take(100)
        .Select(x => new JobResponse(
            x.Id, x.Title, x.Completed, x.Version))
        .ToListAsync(ct);
    return Results.Ok(rows);
});

app.MapGet("/api/jobs/{id:int}", async (
    int id, StudyDb db, CancellationToken ct) =>
{
    var row = await db.Jobs.AsNoTracking()
        .SingleOrDefaultAsync(x => x.Id == id, ct);
    return row is null
        ? Results.NotFound()
        : Results.Ok(new JobResponse(
            row.Id, row.Title, row.Completed, row.Version));
});

app.MapPost("/api/jobs", async (
    CreateJobInput input, StudyDb db, ILogger<Program> logger,
    CancellationToken ct) =>
{
    var title = input.Title?.Trim();
    if (string.IsNullOrEmpty(title) || title.Length > 200)
    {
        return Results.BadRequest(new
        {
            error = "Başlık 1-200 karakter olmalı."
        });
    }

    var job = new StudyJob { Title = title };
    db.Jobs.Add(job);
    await db.SaveChangesAsync(ct);
    logger.LogInformation("Study job created: {JobId}", job.Id);
    return Results.Created($"/api/jobs/{job.Id}",
        new JobResponse(job.Id, job.Title, job.Completed, job.Version));
});

app.MapPut("/api/jobs/{id:int}", async (
    int id, UpdateJobInput input, StudyDb db, CancellationToken ct) =>
{
    var title = input.Title?.Trim();
    if (string.IsNullOrEmpty(title) || title.Length > 200)
    {
        return Results.BadRequest(new
        {
            error = "Başlık 1-200 karakter olmalı."
        });
    }

    var job = await db.Jobs.SingleOrDefaultAsync(x => x.Id == id, ct);
    if (job is null) return Results.NotFound();
    if (job.Version != input.Version)
    {
        return Results.Conflict(new
        {
            error = "İş değişmiş. Yenileyip tekrar deneyin."
        });
    }

    job.Title = title;
    job.Completed = input.Completed;
    job.Version++;
    try
    {
        await db.SaveChangesAsync(ct);
    }
    catch (DbUpdateConcurrencyException)
    {
        return Results.Conflict(new
        {
            error = "Başka işlem işi değiştirdi. Yenileyin."
        });
    }

    return Results.Ok(new JobResponse(
        job.Id, job.Title, job.Completed, job.Version));
});

app.Run();

// WebApplicationFactory testlerinin giriş noktasına erişmesi için:
public partial class Program { }

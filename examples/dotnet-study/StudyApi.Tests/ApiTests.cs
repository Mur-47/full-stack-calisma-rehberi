using System.Net;
using System.Net.Http.Json;
using System.Text;
using System.Text.Json;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using Xunit;

public sealed class ApiTests : IAsyncLifetime
{
    private readonly string _folder = Path.Combine(Path.GetTempPath(), "study-api-" + Guid.NewGuid());
    private WebApplicationFactory<Program> _factory = null!;
    private HttpClient _client = null!;

    public async Task InitializeAsync()
    {
        Directory.CreateDirectory(_folder);
        _factory = new WebApplicationFactory<Program>().WithWebHostBuilder(builder =>
            builder.UseEnvironment("Production").UseSetting("DatabasePath", Path.Combine(_folder, "test.db")));
        _client = _factory.CreateClient();
        using var scope = _factory.Services.CreateScope();
        await scope.ServiceProvider.GetRequiredService<StudyDb>().Database.MigrateAsync();
    }

    public async Task DisposeAsync()
    {
        _client.Dispose();
        await _factory.DisposeAsync();
        Microsoft.Data.Sqlite.SqliteConnection.ClearAllPools();
        Directory.Delete(_folder, recursive: true);
    }

    [Fact]
    public async Task Create_returns_only_response_fields_and_ignores_entity_fields()
    {
        var response = await _client.PostAsJsonAsync("/api/jobs", new { title = "  Örnek görev  ", id = 900, completed = true, version = 99 });
        Assert.Equal(HttpStatusCode.Created, response.StatusCode);
        var row = await response.Content.ReadFromJsonAsync<JsonElement>();
        Assert.Equal(new[] { "completed", "id", "title", "version" }, row.EnumerateObject().Select(x => x.Name).Order().ToArray());
        Assert.Equal("Örnek görev", row.GetProperty("title").GetString());
        Assert.False(row.GetProperty("completed").GetBoolean());
        Assert.Equal(1, row.GetProperty("version").GetInt32());
        var get = await _client.GetAsync(response.Headers.Location);
        Assert.Equal(HttpStatusCode.OK, get.StatusCode);
        Assert.Equal(row.ToString(), (await get.Content.ReadFromJsonAsync<JsonElement>()).ToString());
    }

    [Theory]
    [InlineData("")]
    [InlineData("   ")]
    [InlineData(null)]
    public async Task Invalid_title_is_400(string? title)
    {
        var response = await _client.PostAsJsonAsync("/api/jobs", new { title });
        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
    }

    [Fact]
    public async Task Long_title_is_400()
    {
        var response = await _client.PostAsJsonAsync("/api/jobs", new { title = new string('x', 201) });
        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
    }

    [Fact]
    public async Task Update_changes_version_and_stale_update_is_409()
    {
        var created = await _client.PostAsJsonAsync("/api/jobs", new { title = "Görev" });
        var input = new { title = "Yeni görev", completed = true, version = 1 };
        var update = await _client.PutAsJsonAsync(created.Headers.Location, input);
        Assert.Equal(HttpStatusCode.OK, update.StatusCode);
        var row = await update.Content.ReadFromJsonAsync<JobResponse>();
        Assert.Equal(2, row!.Version);
        Assert.True(row.Completed);
        Assert.Equal(HttpStatusCode.Conflict, (await _client.PutAsJsonAsync(created.Headers.Location, input)).StatusCode);
    }

    [Fact]
    public async Task Missing_job_is_404_and_list_is_an_array()
    {
        Assert.Equal(HttpStatusCode.NotFound, (await _client.GetAsync("/api/jobs/999")).StatusCode);
        var rows = await _client.GetFromJsonAsync<JobResponse[]>("/api/jobs");
        Assert.Empty(rows!);
    }

    [Fact]
    public async Task Windows_style_utf8_json_round_trips()
    {
        using var body = new StringContent("{\"title\":\"Örnek iş şğİı\"}", Encoding.UTF8, "application/json");
        var response = await _client.PostAsync("/api/jobs", body);
        Assert.Equal(HttpStatusCode.Created, response.StatusCode);
        Assert.Equal("Örnek iş şğİı", (await response.Content.ReadFromJsonAsync<JobResponse>())!.Title);
    }

    [Fact]
    public async Task Two_contexts_detect_real_database_concurrency()
    {
        using var scope1 = _factory.Services.CreateScope();
        using var scope2 = _factory.Services.CreateScope();
        var first = scope1.ServiceProvider.GetRequiredService<StudyDb>();
        var second = scope2.ServiceProvider.GetRequiredService<StudyDb>();
        first.Jobs.Add(new StudyJob { Title = "Başlangıç" });
        await first.SaveChangesAsync();
        var a = await first.Jobs.SingleAsync();
        var b = await second.Jobs.SingleAsync();
        a.Version++;
        a.Title = "Birinci";
        await first.SaveChangesAsync();
        b.Version++;
        b.Title = "İkinci";
        await Assert.ThrowsAsync<DbUpdateConcurrencyException>(() => second.SaveChangesAsync());
    }

    [Fact]
    public async Task Unexpected_database_error_returns_generic_problem_details()
    {
        using var scope = _factory.Services.CreateScope();
        var db = scope.ServiceProvider.GetRequiredService<StudyDb>();
        await db.Database.ExecuteSqlRawAsync("DROP TABLE Jobs");
        var response = await _client.GetAsync("/api/jobs");
        Assert.Equal(HttpStatusCode.InternalServerError, response.StatusCode);
        Assert.Equal("application/problem+json", response.Content.Headers.ContentType!.MediaType);
        var text = await response.Content.ReadAsStringAsync();
        var problem = JsonSerializer.Deserialize<JsonElement>(text);
        Assert.Equal(500, problem.GetProperty("status").GetInt32());
        Assert.DoesNotContain("no such table", text);
        Assert.DoesNotContain(_folder, text);
    }

    [Fact]
    public async Task Migration_preserves_existing_data_when_applied_again()
    {
        using var scope = _factory.Services.CreateScope();
        var db = scope.ServiceProvider.GetRequiredService<StudyDb>();
        db.Jobs.Add(new StudyJob { Title = "Korunacak", Completed = true, Version = 3 });
        await db.SaveChangesAsync();
        await db.Database.MigrateAsync();
        db.ChangeTracker.Clear();
        var row = await db.Jobs.SingleAsync();
        Assert.Equal("Korunacak", row.Title);
        Assert.True(row.Completed);
        Assert.Equal(3, row.Version);
    }
}

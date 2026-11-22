using Microsoft.EntityFrameworkCore;

public class StudyJob
{
    public int Id { get; set; }
    public string Title { get; set; } = "";
    public bool Completed { get; set; }
    public int Version { get; set; } = 1;
}

public class StudyDb(DbContextOptions<StudyDb> options)
    : DbContext(options)
{
    public DbSet<StudyJob> Jobs => Set<StudyJob>();

    protected override void OnModelCreating(ModelBuilder model)
    {
        model.Entity<StudyJob>().Property(x => x.Title)
            .HasMaxLength(200);
        model.Entity<StudyJob>().Property(x => x.Version)
            .IsConcurrencyToken();
    }
}

public record JobResponse(int Id, string Title, bool Completed, int Version);
public record CreateJobInput(string? Title);
public record UpdateJobInput(
    string? Title, bool Completed, int Version);

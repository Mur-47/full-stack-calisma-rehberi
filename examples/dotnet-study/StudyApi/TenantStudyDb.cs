using Microsoft.EntityFrameworkCore;

// tenantId doğrulanmış oturumdan gelir. DbContext örneğinde saklanır.
public sealed class TenantStudyDb(
    DbContextOptions<TenantStudyDb> options, Guid tenantId)
    : DbContext(options)
{
    private readonly Guid _tenantId = tenantId;
    public DbSet<TenantJob> Jobs => Set<TenantJob>();

    protected override void OnModelCreating(ModelBuilder model)
    {
        model.Entity<TenantJob>().HasQueryFilter(x =>
            x.TenantId == _tenantId);
    }
}

public sealed class TenantJob
{
    public int Id { get; set; }
    public Guid TenantId { get; set; }
    public string Title { get; set; } = "";
}

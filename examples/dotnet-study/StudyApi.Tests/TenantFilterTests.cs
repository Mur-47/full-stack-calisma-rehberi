using Microsoft.Data.Sqlite;
using Microsoft.EntityFrameworkCore;
using Xunit;

public sealed class TenantFilterTests : IAsyncLifetime
{
    private readonly SqliteConnection _connection = new("Data Source=:memory:");
    private readonly Guid _a = Guid.NewGuid();
    private readonly Guid _b = Guid.NewGuid();
    private DbContextOptions<TenantStudyDb> _options = null!;

    public async Task InitializeAsync()
    {
        await _connection.OpenAsync();
        _options = new DbContextOptionsBuilder<TenantStudyDb>().UseSqlite(_connection).Options;
        await using var db = new TenantStudyDb(_options, _a);
        await db.Database.EnsureCreatedAsync();
        db.Jobs.AddRange(new TenantJob { TenantId = _a, Title = "A" }, new TenantJob { TenantId = _b, Title = "B" });
        await db.SaveChangesAsync();
    }

    public async Task DisposeAsync() => await _connection.DisposeAsync();

    [Fact]
    public async Task Cached_model_uses_each_context_tenant()
    {
        await using var a = new TenantStudyDb(_options, _a);
        await using var b = new TenantStudyDb(_options, _b);
        Assert.Equal("A", (await a.Jobs.SingleAsync()).Title);
        Assert.Equal("B", (await b.Jobs.SingleAsync()).Title);
        Assert.Same(a.Model, b.Model);
    }

    [Fact]
    public async Task ExecuteUpdate_keeps_query_filter_but_bypasses_tracked_values()
    {
        await using var a = new TenantStudyDb(_options, _a);
        var tracked = await a.Jobs.SingleAsync();
        Assert.Equal(1, await a.Jobs.ExecuteUpdateAsync(x => x.SetProperty(j => j.Title, "A2")));
        Assert.Equal("A", tracked.Title);
        await using var b = new TenantStudyDb(_options, _b);
        Assert.Equal("B", (await b.Jobs.SingleAsync()).Title);
    }

    [Fact]
    public async Task ExecuteDelete_keeps_query_filter()
    {
        await using var a = new TenantStudyDb(_options, _a);
        Assert.Equal(1, await a.Jobs.ExecuteDeleteAsync());
        await using var b = new TenantStudyDb(_options, _b);
        Assert.Equal("B", (await b.Jobs.SingleAsync()).Title);
    }

    [Fact]
    public async Task Raw_sql_does_not_add_tenant_filter()
    {
        await using var a = new TenantStudyDb(_options, _a);
        Assert.Equal(2, await a.Database.ExecuteSqlAsync($"UPDATE Jobs SET Title = {"SQL"}"));
        await using var b = new TenantStudyDb(_options, _b);
        Assert.Equal("SQL", (await b.Jobs.SingleAsync()).Title);
    }

    [Fact]
    public async Task Query_filter_alone_does_not_validate_new_rows()
    {
        await using var a = new TenantStudyDb(_options, _a);
        a.Jobs.Add(new TenantJob { TenantId = _b, Title = "Yazma denetimi gerekli" });
        await a.SaveChangesAsync();
        await using var b = new TenantStudyDb(_options, _b);
        Assert.Equal(2, await b.Jobs.CountAsync());
    }
}

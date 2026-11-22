using Xunit;

public sealed class WorkshopTests
{
    [Fact]
    public void Work_item_rejects_negative_minutes_without_changing_state()
    {
        var item = new WorkItem("  Test görevi  ");
        item.AddMinutes(20);
        Assert.Throws<ArgumentOutOfRangeException>(() => item.AddMinutes(-5));
        Assert.Equal(20, item.Minutes);
        Assert.Equal("Test görevi", item.Title);
    }

    [Fact]
    public void Work_item_rejects_blank_title()
    {
        Assert.Throws<ArgumentException>(() => new WorkItem(" "));
    }

    [Fact]
    public void Generic_page_and_linq_preserve_expected_result()
    {
        var items = new[] { (Title: "A", Minutes: 20), (Title: "B", Minutes: 5), (Title: "C", Minutes: 35) };
        var titles = items.Where(x => x.Minutes >= 20).OrderByDescending(x => x.Minutes).Select(x => x.Title).ToArray();
        var page = new Page<string>(titles, titles.Length);
        Assert.Equal(new[] { "C", "A" }, page.Items);
        Assert.Equal(2, page.Total);
    }

    [Fact]
    public void Interface_can_supply_fixed_time()
    {
        var now = DateTimeOffset.Parse("2026-11-23T00:00:00Z");
        IClock clock = new FixedClock(now);
        Assert.Equal(now, clock.UtcNow);
    }
}

public sealed class WorkItem
{
    public string Title { get; }
    public int Minutes { get; private set; }

    public WorkItem(string title)
    {
        if (string.IsNullOrWhiteSpace(title))
            throw new ArgumentException("Başlık gerekli.", nameof(title));
        Title = title.Trim();
    }

    public void AddMinutes(int minutes)
    {
        if (minutes <= 0)
            throw new ArgumentOutOfRangeException(nameof(minutes));
        Minutes = checked(Minutes + minutes);
    }
}

public interface IClock
{
    DateTimeOffset UtcNow { get; }
}

public sealed class FixedClock(DateTimeOffset value) : IClock
{
    public DateTimeOffset UtcNow => value;
}

public record Page<T>(IReadOnlyList<T> Items, int Total);

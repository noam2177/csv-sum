import csv
import io


def bounds(numbers: list[int]) -> tuple[int, int]:
    """Smallest and largest value. An empty column is 0 and 0."""
    if not numbers:
        return 0, 0
    return min(numbers), max(numbers)


def median(numbers: list[int]) -> float:
    """Middle value. An even count averages the two middle values. Empty is 0."""
    if not numbers:
        return 0.0
    ordered = sorted(numbers)
    count = len(ordered)
    if count % 2 == 1:
        return float(ordered[count // 2])
    return (ordered[count // 2 - 1] + ordered[count // 2]) / 2.0


def _stdev(numbers: list[int]) -> float:
    if len(numbers) < 2:
        return 0.0
    center = sum(numbers) / len(numbers)
    variance = sum((value - center) ** 2 for value in numbers) / (len(numbers) - 1)
    return variance ** 0.5


def report_csv(text: str) -> str:
    rows = list(csv.DictReader(io.StringIO(text)))
    numbers = [int(row["n"]) for row in rows if row.get("n")]
    total = sum(numbers)
    mean = (total / len(numbers)) if numbers else 0.0
    spread = _stdev(numbers)
    mid = median(numbers)
    low, high = bounds(numbers)
    return (
        f"rows={len(rows)},sum={total},mean={mean:.3f},median={mid:.3f},"
        f"min={low},max={high},stdev={spread:.3f}"
    )

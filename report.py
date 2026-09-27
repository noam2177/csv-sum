import csv
import io


def report_csv(text: str) -> str:
    rows = list(csv.DictReader(io.StringIO(text)))
    numbers = [int(row["n"]) for row in rows if row.get("n")]
    total = sum(numbers)
    mean = (total / len(numbers)) if numbers else 0.0
    return f"rows={len(rows)},sum={total},mean={mean:.3f}"

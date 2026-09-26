import csv
import io


def report_csv(text: str) -> str:
    rows = list(csv.DictReader(io.StringIO(text)))
    total = sum(int(row["n"]) for row in rows if row.get("n"))
    return f"rows={len(rows)},sum={total}"

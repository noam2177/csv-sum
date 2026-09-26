import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from report import report_csv


class TestReportCsv(unittest.TestCase):
    def test_basic(self) -> None:
        text = "name,n\na,1\nb,2\nc,3"
        self.assertEqual(report_csv(text), "rows=3,sum=6")

    def test_header_only(self) -> None:
        self.assertEqual(report_csv("name,n"), "rows=0,sum=0")

    def test_blank_n_counts_as_a_row(self) -> None:
        text = "name,n\na,\nb,4"
        self.assertEqual(report_csv(text), "rows=2,sum=4")


if __name__ == "__main__":
    unittest.main()

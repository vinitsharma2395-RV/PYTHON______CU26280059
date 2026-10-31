import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Copy all CSV rows into another CSV file
(DATA_DIR / "source.csv").write_text("Name,Marks\nAman,85\nRiya,92\n", encoding="utf-8")
with open(DATA_DIR / "source.csv", newline="", encoding="utf-8") as source:
    rows = list(csv.reader(source))
with open(DATA_DIR / "copy.csv", "w", newline="", encoding="utf-8") as target:
    csv.writer(target).writerows(rows)
print("CSV data copied to copy.csv")

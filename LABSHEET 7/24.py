import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Count CSV rows (excluding header) and columns
with open(DATA_DIR / "students.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows([["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92]])
with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
    rows = list(csv.reader(file))
print("Data rows:", max(0, len(rows)-1))
print("Columns:", len(rows[0]) if rows else 0)

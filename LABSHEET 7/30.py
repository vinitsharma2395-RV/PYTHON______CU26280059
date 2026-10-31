import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Combine multiple CSV files with the same columns
sample_files = {
    "class_a.csv": [["Name", "Marks"], ["Aman", 85]],
    "class_b.csv": [["Name", "Marks"], ["Riya", 92]],
}
for filename, rows in sample_files.items():
    with open(DATA_DIR / filename, "w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerows(rows)
combined = []
for filename in ["class_a.csv", "class_b.csv"]:
    with open(DATA_DIR / filename, newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
        combined.extend(rows if not combined else rows[1:])
with open(DATA_DIR / "all_students.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows(combined)
print("Combined", len(combined) - 1, "records into all_students.csv")

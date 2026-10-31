import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Display selected columns: Name and Marks
rows = [["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92]]
with open(DATA_DIR / "students.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows(rows)
with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print("Name:", row["Name"], "| Marks:", row["Marks"])

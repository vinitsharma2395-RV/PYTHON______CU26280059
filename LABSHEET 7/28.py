import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Find the student with the highest marks
rows = [{"Name": "Aman", "Marks": "85"}, {"Name": "Riya", "Marks": "92"}, {"Name": "Karan", "Marks": "78"}]
with open(DATA_DIR / "students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Marks"])
    writer.writeheader(); writer.writerows(rows)
with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
    data = list(csv.DictReader(file))
if data:
    best = max(data, key=lambda row: float(row["Marks"]))
    print("Highest scorer:", best["Name"], "-", best["Marks"])

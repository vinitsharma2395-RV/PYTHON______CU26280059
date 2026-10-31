import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Search a CSV record by student name
rows = [{"Name": "Aman", "Marks": "85"}, {"Name": "Riya", "Marks": "92"}]
with open(DATA_DIR / "students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Marks"])
    writer.writeheader(); writer.writerows(rows)
search_name = input("Enter student name: ").strip().lower()
with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
    matches = [row for row in csv.DictReader(file) if row["Name"].lower() == search_name]
print(matches if matches else "Record not found.")

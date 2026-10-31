import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Create a CSV file and write student records
rows = [["Name", "Age", "Marks"], ["Aman", 20, 85], ["Riya", 21, 92], ["Karan", 19, 78]]
with open(DATA_DIR / "students.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows(rows)
print("students.csv created with", len(rows)-1, "records.")

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Read and display CSV data
with open(DATA_DIR / "students.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows([["Name", "Marks"], ["Aman", 85], ["Riya", 92]])
with open(DATA_DIR / "students.csv", newline="", encoding="utf-8") as file:
    for row in csv.reader(file):
        print(" | ".join(row))

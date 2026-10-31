import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Append one record to an existing CSV file
with open(DATA_DIR / "students.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerow(["Name", "Marks"])
name = input("Student name: ")
marks = input("Marks: ")
with open(DATA_DIR / "students.csv", "a", newline="", encoding="utf-8") as file:
    csv.writer(file).writerow([name, marks])
print("Record appended successfully.")

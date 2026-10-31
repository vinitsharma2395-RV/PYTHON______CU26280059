import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

# Calculate average of numeric CSV columns
rows = [["Name", "Maths", "Science"], ["Aman", 80, 90], ["Riya", 90, 95], ["Karan", 70, 85]]
with open(DATA_DIR / "marks.csv", "w", newline="", encoding="utf-8") as file:
    csv.writer(file).writerows(rows)
with open(DATA_DIR / "marks.csv", newline="", encoding="utf-8") as file:
    data = list(csv.DictReader(file))
for column in ["Maths", "Science"]:
    values = [float(row[column]) for row in data]
    print(f"Average {column}: {sum(values)/len(values):.2f}")

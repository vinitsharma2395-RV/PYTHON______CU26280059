import csv
from db_helper import DATA_DIR, connect_db

# Import records from CSV into students table
with open(DATA_DIR / "students_import.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "marks"])
    writer.writerows([["Isha", 20, 89], ["Rahul", 22, 81]])
with open(DATA_DIR / "students_import.csv", newline="", encoding="utf-8") as file:
    records = [
        (row["name"], int(row["age"]), float(row["marks"]))
        for row in csv.DictReader(file)
    ]
with connect_db() as con:
    con.executemany(
        "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", records
    )
print("Imported", len(records), "records.")

import csv
from db_helper import DATA_DIR, connect_db

# Export all student records to CSV
with connect_db() as con: rows = con.execute("SELECT id, name, age, marks FROM students").fetchall()
with open(DATA_DIR / "students_export.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file); writer.writerow(["id", "name", "age", "marks"]); writer.writerows(rows)
print("Exported", len(rows), "records to students_export.csv")

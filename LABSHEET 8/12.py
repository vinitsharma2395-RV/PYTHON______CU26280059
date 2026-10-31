from db_helper import connect_db
# Retrieve students whose marks are greater than 80
with connect_db() as con:
    rows = con.execute("SELECT * FROM students WHERE marks > ?", (80,)).fetchall()
for row in rows: print(row)
if not rows: print("No student scored above 80.")

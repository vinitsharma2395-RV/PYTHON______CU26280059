from db_helper import connect_db
# Display only name and marks columns
with connect_db() as con:
    rows = con.execute("SELECT name, marks FROM students").fetchall()
for name, marks in rows: print(f"Name: {name} | Marks: {marks}")

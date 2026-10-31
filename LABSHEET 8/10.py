from db_helper import connect_db
# Read and display all student records
with connect_db() as con:
    rows = con.execute("SELECT * FROM students ORDER BY id").fetchall()
for row in rows: print(row)
if not rows: print("No records found.")

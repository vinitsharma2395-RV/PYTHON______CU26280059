from db_helper import connect_db
# Sort students by marks in descending order
with connect_db() as con:
    rows = con.execute("SELECT * FROM students ORDER BY marks DESC").fetchall()
for row in rows: print(row)

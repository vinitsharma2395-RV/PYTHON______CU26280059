from db_helper import connect_db
# Display the top three highest-scoring students
with connect_db() as con:
    rows = con.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3").fetchall()
for rank, row in enumerate(rows, start=1): print(rank, row)

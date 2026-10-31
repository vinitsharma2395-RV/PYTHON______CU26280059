from db_helper import connect_db
# Calculate average marks of all students
with connect_db() as con:
    average = con.execute("SELECT AVG(marks) FROM students").fetchone()[0]
print("Average marks:", round(average, 2) if average is not None else "No records")

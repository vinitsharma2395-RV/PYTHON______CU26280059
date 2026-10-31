from db_helper import connect_db
# Group students by age and count students in each group
with connect_db() as con:
    rows = con.execute("SELECT age, COUNT(*) FROM students GROUP BY age ORDER BY age").fetchall()
for age, total in rows: print(f"Age {age}: {total} student(s)")

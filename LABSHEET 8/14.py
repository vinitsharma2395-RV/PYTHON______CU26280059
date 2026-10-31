from db_helper import connect_db
# Count total student records
with connect_db() as con:
    total = con.execute("SELECT COUNT(*) FROM students").fetchone()[0]
print("Total students:", total)

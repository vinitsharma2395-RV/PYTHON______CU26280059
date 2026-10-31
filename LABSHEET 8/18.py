from db_helper import connect_db

# Delete one student using ID
try:
    student_id = int(input("Student ID to delete: "))
    with connect_db() as con:
        cur = con.execute("DELETE FROM students WHERE id = ?", (student_id,))
    print("Record deleted." if cur.rowcount else "Student ID not found.")
except ValueError:
    print("Student ID must be a whole number.")

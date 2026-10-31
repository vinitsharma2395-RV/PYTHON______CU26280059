from db_helper import connect_db

# Update student name by ID
try:
    student_id = int(input("Student ID: "))
    new_name = input("New name: ").strip()
    if not new_name:
        print("Name cannot be empty.")
    else:
        with connect_db() as con:
            cur = con.execute(
                "UPDATE students SET name = ? WHERE id = ?",
                (new_name, student_id),
            )
        print("Name updated." if cur.rowcount else "Student ID not found.")
except ValueError:
    print("Student ID must be a whole number.")

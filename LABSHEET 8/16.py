from db_helper import connect_db

# Update marks by student ID
try:
    student_id = int(input("Student ID: "))
    new_marks = float(input("New marks (0-100): "))
    if not 0 <= new_marks <= 100:
        print("Marks must be from 0 to 100.")
    else:
        with connect_db() as con:
            cur = con.execute(
                "UPDATE students SET marks = ? WHERE id = ?",
                (new_marks, student_id),
            )
        print("Marks updated." if cur.rowcount else "Student ID not found.")
except ValueError:
    print("Student ID must be a whole number and marks must be numeric.")

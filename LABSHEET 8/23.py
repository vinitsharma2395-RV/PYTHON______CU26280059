from db_helper import connect_db

# LEFT JOIN: show every student, even without a matching course
with connect_db() as con:
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL
        )
        """
    )
    con.execute("INSERT OR IGNORE INTO courses VALUES (1, 'Python')")
    columns = {row[1] for row in con.execute("PRAGMA table_info(students)")}
    if "course_id" not in columns:
        con.execute("ALTER TABLE students ADD COLUMN course_id INTEGER")
    first_student_id = con.execute("SELECT MIN(id) FROM students").fetchone()[0]
    if first_student_id is not None:
        con.execute(
            "UPDATE students SET course_id = 1 WHERE id = ?",
            (first_student_id,),
        )
    rows = con.execute(
        """
        SELECT students.name, courses.course_name
        FROM students
        LEFT JOIN courses ON students.course_id = courses.course_id
        ORDER BY students.id
        """
    ).fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("No student records found.")

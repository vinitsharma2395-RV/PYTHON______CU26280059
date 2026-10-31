from db_helper import connect_db

# Create courses table and insert sample course data
with connect_db() as con:
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL
        )
        """
    )
    courses = [(1, "Python"), (2, "Database Systems"), (3, "Web Design")]
    con.executemany(
        "INSERT OR IGNORE INTO courses (course_id, course_name) VALUES (?, ?)",
        courses,
    )
print("Courses table created and sample courses inserted.")

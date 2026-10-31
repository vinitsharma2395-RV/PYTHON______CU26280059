# Q19: Find the student with the highest marks
import sqlite3
from db_helper import connect_db

connection = None
try:
    connection = connect_db()
    row = connection.execute(
        "SELECT id, name, age, marks FROM students ORDER BY marks DESC LIMIT 1"
    ).fetchone()

    if row:
        print("Student with highest marks:", row)
    else:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()

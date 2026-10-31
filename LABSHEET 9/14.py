# Q14: Search for a student by roll number
import sqlite3
from db_helper import connect_db

connection = None
try:
    connection = connect_db()
    roll_no = int(input("Enter roll number/ID to search: "))
    row = connection.execute(
        "SELECT id, name, age, marks FROM students WHERE id = ?", (roll_no,)
    ).fetchone()

    if row:
        print("Student found:", row)
    else:
        print("Student not found.")
except ValueError:
    print("Roll number must be numeric.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()

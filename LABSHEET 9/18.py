# Q18: Display all students sorted by name
import sqlite3
from db_helper import connect_db

connection = None
try:
    connection = connect_db()
    rows = connection.execute(
        "SELECT id, name, age, marks FROM students ORDER BY name ASC"
    ).fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No student records found.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()

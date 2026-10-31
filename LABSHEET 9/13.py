# Q13: Read and display all student records
import sqlite3
from db_helper import connect_db

connection = None
try:
    connection = connect_db()
    rows = connection.execute("SELECT id, name, age, marks FROM students ORDER BY id").fetchall()
    if rows:
        print("ID | Name | Age | Marks")
        for row in rows:
            print(*row, sep=" | ")
    else:
        print("No student records found. Run Q12 to insert records.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()

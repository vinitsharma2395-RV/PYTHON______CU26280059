# Q15: Update student marks using roll number
import sqlite3
from db_helper import connect_db

connection = None
try:
    connection = connect_db()
    roll_no = int(input("Enter roll number/ID: "))
    new_marks = float(input("Enter new marks: "))

    cursor = connection.execute(
        "UPDATE students SET marks = ? WHERE id = ?", (new_marks, roll_no)
    )
    connection.commit()
    print("Marks updated successfully." if cursor.rowcount else "Student not found.")
except ValueError:
    print("Enter valid numeric values.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()

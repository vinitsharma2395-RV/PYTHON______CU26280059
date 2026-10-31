# Q16: Delete a student record using roll number
import sqlite3
from db_helper import connect_db

connection = None
try:
    connection = connect_db()
    roll_no = int(input("Enter roll number/ID to delete: "))
    cursor = connection.execute("DELETE FROM students WHERE id = ?", (roll_no,))
    connection.commit()
    print("Student record deleted successfully." if cursor.rowcount else "Student not found.")
except ValueError:
    print("Roll number must be numeric.")
except sqlite3.Error as error:
    print("Database error:", error)
finally:
    if connection:
        connection.close()

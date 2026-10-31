import sqlite3

from db_helper import connect_db

# Menu-driven student management application
while True:
    print("\n--- STUDENT MANAGEMENT ---")
    print("1. Add student")
    print("2. View students")
    print("3. Update student marks")
    print("4. Delete student")
    print("5. Exit")
    choice = input("Choose: ").strip()
    try:
        if choice == "1":
            name = input("Name: ").strip()
            age = int(input("Age: "))
            marks = float(input("Marks (0-100): "))
            if not name or age < 0 or not 0 <= marks <= 100:
                print("Enter a name, a non-negative age, and marks from 0 to 100.")
                continue
            with connect_db() as con:
                con.execute(
                    "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
                    (name, age, marks),
                )
            print("Student added.")
        elif choice == "2":
            with connect_db() as con:
                rows = con.execute("SELECT * FROM students ORDER BY id").fetchall()
            if rows:
                for row in rows:
                    print(row)
            else:
                print("No records.")
        elif choice == "3":
            student_id = int(input("ID: "))
            marks = float(input("New marks (0-100): "))
            if not 0 <= marks <= 100:
                print("Marks must be from 0 to 100.")
                continue
            with connect_db() as con:
                cur = con.execute(
                    "UPDATE students SET marks = ? WHERE id = ?",
                    (marks, student_id),
                )
            print("Updated." if cur.rowcount else "ID not found.")
        elif choice == "4":
            student_id = int(input("ID: "))
            with connect_db() as con:
                cur = con.execute("DELETE FROM students WHERE id = ?", (student_id,))
            print("Deleted." if cur.rowcount else "ID not found.")
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Enter valid numeric values.")
    except sqlite3.Error as error:
        print("Database operation failed:", error)

from db_helper import connect_db

# Insert one student using a parameterized query
try:
    name = input("Name: ").strip()
    age = int(input("Age: "))
    marks = float(input("Marks (0-100): "))
    if not name or age < 0 or not 0 <= marks <= 100:
        print("Enter a name, a non-negative age, and marks from 0 to 100.")
    else:
        with connect_db() as con:
            cur = con.execute(
                "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
                (name, age, marks),
            )
        print("Inserted student ID:", cur.lastrowid)
except ValueError:
    print("Age must be a whole number and marks must be numeric.")

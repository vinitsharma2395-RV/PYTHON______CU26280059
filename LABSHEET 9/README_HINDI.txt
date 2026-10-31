PYTHON PROGRAMMING LAB SHEET 09 - CRUD OPERATIONS

CONTENTS
- 1.py to 20.py: Programs in question order; 1.py is Question 1, and 20.py is
  Question 20.
- Q01-Q05: Student records stored in Python lists.
- Q06: Employee CRUD using a dictionary.
- Q07-Q08: Book and product CRUD using lists and menus.
- Q09-Q10: Student records stored in text files.
- Q11-Q20: Student database exercises using SQLite.
- db_helper.py: Shared database connection and table setup.

RUN A PROGRAM
From the workspace folder, run a file with Python, for example:
    python "LABSHEET 9/1.py"

The programs use Python's standard library. No extra packages are required.
For the database questions, db_helper.py creates the students table when a
program opens the database. Run 12.py to add a record before 13.py-20.py if the
database does not contain students yet.

WHERE DATA IS STORED
- Q01-Q08: In memory; changes disappear when the program exits.
- Q09-Q10: In text files beside the scripts; records remain between runs.
- Q11-Q20: In student_db.db beside db_helper.py; records remain between runs.

PRESENTATION TIP
For each question, explain where the data is stored, run the program, and show
the output. For update and delete questions, show the record before and after.

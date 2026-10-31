PYTHON PROGRAMMING LAB SHEET 08 - SQLITE DATABASE

CONTENTS
- 1.py to 30.py: SQLite database exercises (in question order).
- db_helper.py: Shared connection and database setup functions.
- student_db.db: The database used by these exercises; it is created when
  needed in this folder.

SET UP AND RUN
SQLite is included with Python. No separate database server or package is
needed. From the workspace folder, initialize example student records once:
    python "LABSHEET 8/db_helper.py"

Then run a question, for example:
    python "LABSHEET 8/14.py"

Each program uses the database in this folder, even when launched from the
workspace root. Run one question at a time and inspect the terminal output.

NOTES
- Q08, Q09, Q27, and Q29 insert records. Re-running them adds more records.
- Q06 can permanently drop the students or courses table after confirmation.
- Q20 permanently deletes all student records after confirmation.
- Q21-Q23 demonstrate course tables and joins. Q22 adds a course_id column to
  the students table when it is not already present.
- To start over, close programs and remove this folder's student_db.db file,
  then run db_helper.py again. This also removes any records you added.

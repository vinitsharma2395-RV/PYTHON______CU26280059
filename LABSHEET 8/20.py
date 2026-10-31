from db_helper import connect_db
# Empty table but keep its structure (SQLite equivalent of TRUNCATE)
confirm = input("Type YES to delete every student record: ")
if confirm == "YES":
    with connect_db() as con:
        con.execute("DELETE FROM students")
    print("Table is empty; its structure is preserved.")
else: print("Operation cancelled.")

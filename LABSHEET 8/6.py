from db_helper import connect_db
# Drop a table only after explicit confirmation
name = input("Enter table name to drop (students/courses): ").strip()
confirm = input(f"Type YES to permanently drop {name}: ")
if name in {"students", "courses"} and confirm == "YES":
    with connect_db() as con: con.execute(f'DROP TABLE IF EXISTS "{name}"')
    print("Table dropped.")
else: print("Cancelled or invalid table name.")

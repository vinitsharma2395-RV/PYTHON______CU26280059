from db_helper import connect_db
# Display table structure using PRAGMA
with connect_db() as con:
    for column in con.execute("PRAGMA table_info(students)"):
        print(column)

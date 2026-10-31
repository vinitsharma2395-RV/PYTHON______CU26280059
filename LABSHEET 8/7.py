from db_helper import connect_db
# Check whether a table exists
name = input("Enter table name: ").strip()
with connect_db() as con:
    result = con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone()
print("Table exists." if result else "Table does not exist.")

from db_helper import connect_db
# List all tables in the current database
with connect_db() as con:
    tables = con.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
    print("Tables:")
    for table in tables: print("-", table[0])

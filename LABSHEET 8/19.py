from db_helper import connect_db
# Delete students scoring below 40
with connect_db() as con:
    cur = con.execute("DELETE FROM students WHERE marks < ?", (40,))
print("Students deleted:", cur.rowcount)

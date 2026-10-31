from db_helper import connect_db
# Insert multiple student records together
records = [("Aarav",20,88),("Meera",21,91),("Dev",19,76)]
with connect_db() as con:
    con.executemany("INSERT INTO students(name, age, marks) VALUES (?, ?, ?)", records)
print("Inserted", len(records), "records.")

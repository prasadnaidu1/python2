import sqlite3 as sql
conn=sql.connect("satya.db")
cursor=conn.cursor()
try:
    cursor.execute("insert into employee values(101)")
except sql.OperationalError as oe:
    print(oe)
finally:
    cursor.close()
    conn.close()
    print("connection are closed")
print("Thnaks")
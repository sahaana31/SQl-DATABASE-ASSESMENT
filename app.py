import sqlite3

db = sqlite3.connect("Members.db")
cursor = db.cursor()
sql = "SELECT * from members;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close
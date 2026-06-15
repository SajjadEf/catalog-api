import sqlite3

connection = sqlite3.connect("catalog2.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM catalog")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()

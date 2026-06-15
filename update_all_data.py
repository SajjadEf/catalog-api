import sqlite3

connection = sqlite3.connect("catalog2.db")

cursor = connection.cursor()

cursor.execute ('''
    UPDATE catalog
                SET price = price * 1.1
''')

connection.commit()
connection.close()

print("data updated")
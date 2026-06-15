import sqlite3

connection = sqlite3.connect("catalog2.db")

cursor = connection.cursor()

cursor.execute ('''
    UPDATE catalog
                SET price = 65000
                WHERE name = 'docheshme'
''')

connection.commit()
connection.close()

print("data updated")
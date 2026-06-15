import sqlite3

connection = sqlite3.connect("catalog2.db")
cursor = connection.cursor()

cursor.execute('''
    DELETE FROM catalog 
       WHERE name = 'docheshme'
''')

connection.commit()
connection.close()

print("data inserted")
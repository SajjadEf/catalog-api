import sqlite3


connection = sqlite3.connect("catalog2.db")

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS catalog(
    name TEXT PRIMARY KEY,
    price REAL,
    number_in_box INTEGER,
    total_inventory INTEGER
)



''')

connection.commit()
connection.close()
print("table is created")
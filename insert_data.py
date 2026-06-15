import sqlite3

connection = sqlite3.connect("catalog2.db")
cursor = connection.cursor()

cursor.execute('''
    INSERT INTO catalog (name , price, number_in_box,total_inventory)
            VALUES ('docheshme',60000 , 43, 80)
''')

connection.commit()
connection.close()

print("data inserted")
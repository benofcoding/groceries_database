import sqlite3

DATABASE = 'groceries.db'

def print_main_table():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM groceries"
    cursor.execute(sql)
    results = cursor.fetchall()
    for grocerie in results:
        print(f"{grocerie[0]:<5}{grocerie[1]:<65}{grocerie[2]}")
    db.close()

print_main_table()
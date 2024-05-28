import sqlite3

DATABASE = 'groceries.db'

def print_main_table():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM groceries"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(" id    Name                                                                Brand  CPS     servings   GPS     cost    type")
    for grocerie in results:
        print(f"| {grocerie[0]:<2} | {grocerie[1]:<65} | {grocerie[2]:<4} | {grocerie[3]:<5} | {grocerie[4]:<8} | {grocerie[5]:<5} | {grocerie[6]:<5} | {grocerie[7]:<5} |")
    db.close()

print_main_table()
import sqlite3


#constants
DATABASE = 'groceries.db'



def Print_name_ID():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Groceries.ID, Groceries.Name FROM Groceries"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("  ID   Name")
    for grocerie in results:
        print(f"| {grocerie[0]:<2} | {grocerie[1]:<65} |")



def search_for_grocerie():
    Print_name_ID()
    print("")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        try:
            ID = input("Input the ID of the grocerie you would like to see more information about?\n")
            sql = f"SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID WHERE Groceries.ID = '{ID}'"
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) != 0:
                print(results)
            
            db.close()
            break
        except:
            print("Invalid input")




def main_menu():
    print("1. search for a specific item")



    option_chosen = input("what would you like to do?\n")



    all_options = {"1":search_for_grocerie}



    all_options[option_chosen]()

main_menu()
import sqlite3


#constants
DATABASE = 'groceries.db'

Product_ID_Length = 2
Product_Name_Length = 65
Calories_Per_Serving_Length = 3
Servings_Length = 2
Serving_Size_Length = 3
Price_length = 4

Brand_ID_Length = 2
Brand_Name_Length = 15

Product_Type_ID_Length = 2
Product_Type_Length = 30



def Print_name_ID():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Groceries.ID, Groceries.Name FROM Groceries"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("  ID   Name")
    for grocery in results:
        print(f"| {grocery[0]:<2} | {grocery[1]:<65} |")



def search_for_grocery():
    Print_name_ID()
    print("")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        try:
            ID = input("Input the ID of the grocery you would like to see more information about?\n")
            sql = f"SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID WHERE Groceries.ID = '{ID}'"
            cursor.execute(sql)
            results = cursor.fetchall()
            if len(results) == 0:
                print("Invalid input")
            else:
                result = results[0]
                print(f"| {result[0]:<{Product_Name_Length}} | {result[1]:<{Price_length}} | {result[2]:<{Serving_Size_Length}} | {result[3]:<{Calories_Per_Serving_Length}} | {result[4]:<{Servings_Length}} | {result[5]:<{Product_Type_Length}} | {result[6]:<{Brand_Name_Length}} |")
            db.close()
            break
        except:
            print("Invalid input")
            print(results)





def main_menu():
    print("1. search for a specific item")
    option_chosen = input("what would you like to do?\n")
    all_options = {"1":search_for_grocery}
    all_options[option_chosen]()

main_menu()





#print("| {} {:>{}} ".format(Product_Name_tag,Gap_tag,len(result[0])+len(Gap_tag)-len(Product_Name_tag)))
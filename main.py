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
                print("| Name                                                              | P(c) | SS  | CPS | S  | Type                           | Brand           |")
                print("-"*144)
                print(f"| {result[0]:<{Product_Name_Length}} | {result[1]:<{Price_length}} | {result[2]:<{Serving_Size_Length}} | {result[3]:<{Calories_Per_Serving_Length}} | {result[4]:<{Servings_Length}} | {result[5]:<{Product_Type_Length}} | {result[6]:<{Brand_Name_Length}} |")
            db.close()
            break
        except:
            print("Invalid input")
            print(results)





def main_menu():
    while True:

        all_options = {"1":search_for_grocery}
        all_options_text = ["| 1.    | Search for a specific item |",
                            "| quit. | Quit the program           |"]
        
        for option in all_options_text:
            print(option)
        
        try:
            
            option_chosen = input("what would you like to do?\n") 
            if str(option_chosen) in all_options:    
                all_options[option_chosen]()
            elif str(option_chosen) == "quit" or "quit." or "Quit" or "Quit.":
                break
            else:
                print("that is not an option")
                
        except:
            print("that is not an option")

main_menu()





#print("| {} {:>{}} ".format(Product_Name_tag,Gap_tag,len(result[0])+len(Gap_tag)-len(Product_Name_tag)))
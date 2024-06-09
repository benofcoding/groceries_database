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



def Print_name_and_ID_for_Groceries():
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run sql quere
    sql = "SELECT Groceries.ID, Groceries.Name FROM Groceries"
    cursor.execute(sql)
    results = cursor.fetchall()
    #print nicely
    print("  ID   Name")
    for grocery in results:
        print(f"| {grocery[0]:<{Product_ID_Length}} | {grocery[1]:<{Product_Name_Length}} |")



def search_for_grocery():
    #show name and id table
    Print_name_and_ID_for_Groceries()
    print("")
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run until finished with quere
    while True:
        #try execpt to catch false ID inputs
        try:
            #get users wanted product to show or go back to main menu if wanted
            ID = input("Input the ID of the grocery you would like to see more information about or input 'back' to go back?\n")
            if ID == "back":
                main_menu()
            #run sql quere
            sql = f"SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID WHERE Groceries.ID = '{ID}'"
            cursor.execute(sql)
            results = cursor.fetchall()
            #if the ID requested is out of range print invalid id
            if len(results) == 0:
                print("Invalid input")
            else:
                #print the acronyms key for column names
                Acronmys = ["P(c) = Price in cents",
                            "SS = Servin size in grams",
                            "CPS = Calories per serving",
                            "S = servings"]
                print("")
                for acromyn in Acronmys:
                    print(acromyn)
                #print the table and columns nicely
                print("")
                result = results[0]
                print("| Name                                                              | P(c) | SS  | CPS | S  | Type                           | Brand           |")
                print("-"*144)
                print(f"| {result[0]:<{Product_Name_Length}} | {result[1]:<{Price_length}} | {result[2]:<{Serving_Size_Length}} | {result[3]:<{Calories_Per_Serving_Length}} | {result[4]:<{Servings_Length}} | {result[5]:<{Product_Type_Length}} | {result[6]:<{Brand_Name_Length}} |")
                print("-"*144)
                print("")
                #stop the function
                db.close()
                break   
        except:
            #if the id inputed wasnt an integer print string:
            print("Invalid input")





def ORDER_BY():
    options = {"1":"Groceries.price_c",
                        "2":"Groceries.Serving_Size_g",
                        "3":"Groceries.Calories_Per_Serving",
                        "4":"Groceries.Servings"}
    
    options_text = ["| 1. | Price                |",
                    "| 2. | Serving_size         |",
                    "| 3. | Calorise per serving |",
                    "| 4. | Sevings              |"]

    for option in options_text:
        print(option)
    print("")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    while True:
        try:
            Sort_by = input("either input the ID of what you would like to sort by or input 'back' to go back.\n")
            if Sort_by == "back":
                main_menu()

            sql = f"SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID ORDER BY {options[Sort_by]} DESC"
            cursor.execute(sql)
            results = cursor.fetchall()

            
            Acronmys = ["P(c) = Price in cents",
                        "SS = Servin size in grams",
                        "CPS = Calories per serving",
                        "S = servings"]
            print("")
            for acromyn in Acronmys:
                print(acromyn)
            print("")
            print("| Name                                                              | P(c) | SS  | CPS | S  | Type                           | Brand           |")
            print("-"*144)
            for result in results:
                print(f"| {result[0]:<{Product_Name_Length}} | {result[1]:<{Price_length}} | {result[2]:<{Serving_Size_Length}} | {result[3]:<{Calories_Per_Serving_Length}} | {result[4]:<{Servings_Length}} | {result[5]:<{Product_Type_Length}} | {result[6]:<{Brand_Name_Length}} |")
            print("-"*144)
            db.close()
        except:
            print("Invalid input")





def show_greaterthan_or_smallerthan():
    options = {"1":"Groceries.price_c",
               "2":"Groceries.Serving_Size_g",
               "3":"Groceries.Calories_Per_Serving",
               "4":"Groceries.Servings"}
    
    options_text = ["| 1. | Price                |",
                    "| 2. | Serving_size         |",
                    "| 3. | Calorise per serving |",
                    "| 4. | Sevings              |"]


    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        for option in options_text:
            print(option)
        print("")

        column = int(input("input the ID of the column you want to sort. If you want to go back to main menu input 'back'.\n"))
        if column == "back":
            main_menu()
        elif column == 1 or column == 2 or column == 3 or column == 4:
            break
        else:
            print("that is not a valid input")
            print("")

    while True:  
        operator = int(input("Would you like to sort by greater than or less than?, input 1 or 2. If you want to go back to main menu input 'back'.\n"))
        if operator == "back":
            main_menu()
        elif int(operator) == 1 or operator == 2:
            break
        else:
            print("that is not a valid input")
                
    while True:
        try:
            value = int(input("what value would you like to sort by? If you want to go back to main menu input 'back'.\n"))
            if value == "back":
                main_menu()
            sql = f"SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID WHERE {options[str(column)]} > {value}"
            cursor.execute(sql)
            results = cursor.fetchall()
            print(options[str(column)])
            
            
            Acronmys = ["P(c) = Price in cents",
                        "SS = Servin size in grams",
                        "CPS = Calories per serving",
                        "S = servings"]
            print("")
            for acromyn in Acronmys:
                print(acromyn)
            print("")
            print("| Name                                                              | P(c) | SS  | CPS | S  | Type                           | Brand           |")
            print("-"*144)
            for result in results:
                print(f"| {result[0]:<{Product_Name_Length}} | {result[1]:<{Price_length}} | {result[2]:<{Serving_Size_Length}} | {result[3]:<{Calories_Per_Serving_Length}} | {result[4]:<{Servings_Length}} | {result[5]:<{Product_Type_Length}} | {result[6]:<{Brand_Name_Length}} |")
            print("-"*144)
            print("")
            db.close()
            break
        
        except:
            print("that is not a valid input")
        


            
       





def main_menu():
    while True:

        all_options = {"1":search_for_grocery,
                       "2":ORDER_BY,
                       "3":show_greaterthan_or_smallerthan}
        all_options_text = ["| 1.    | Search for a specific item                      |",
                            "| 2.    | sort by a specific data type                    |",
                            "| 3.    | sort any column by greater than or smaller than |",
                            "| quit. | Quit the program                                |"]
        
        for option in all_options_text:
            print(option)
        
        try:
            
            option_chosen = input("what would you like to do?\n") 
            if str(option_chosen) in all_options:    
                all_options[option_chosen]()
            elif str(option_chosen).lower() ==  "quit." or "quit":
                break
            else:
                print("that is not an option")
                
        except:
            print("that is not an option")

main_menu()
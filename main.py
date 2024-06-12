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
Product_Type_Length = 25

#all functions
def print_whole_table():
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run sql quere
    sql = "SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID"
    cursor.execute(sql)
    results = cursor.fetchall()
    #print nicely
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

def Print_producttype_and_ID_for_products():
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run sql quere
    sql = "SELECT Product_type.ID, Product_type.Type FROM Product_Type"
    cursor.execute(sql)
    results = cursor.fetchall()
    #print nicely
    print("| ID | Brand                     |")
    print("-"*34)
    for product in results:
        print(f"| {product[0]:<{Product_Type_ID_Length}} | {product[1]:<{Product_Type_Length}} |")
    print("-"*34)

def Print_name_and_ID_for_Groceries():
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run sql quere
    sql = "SELECT Groceries.ID, Groceries.Name FROM Groceries"
    cursor.execute(sql)
    results = cursor.fetchall()
    #print nicely
    print("| ID | Name                                                              |")
    print("-"*74)
    for grocery in results:
        print(f"| {grocery[0]:<{Product_ID_Length}} | {grocery[1]:<{Product_Name_Length}} |")
    print("-"*74)

def Print_brand_and_ID_for_brands():
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run sql quere
    sql = "SELECT Brand.ID, Brand.Name FROM Brand"
    cursor.execute(sql)
    results = cursor.fetchall()
    #print nicely
    print("| ID | Brand           |")
    print("-"*24)
    for brand in results:
        print(f"| {brand[0]:<{Brand_ID_Length}} | {brand[1]:<{Brand_Name_Length}} |")
    print("-"*24)

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
                print("")
                print("Invalid input")
                print("")
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
            print("")
            print("Invalid input")
            print("")

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
        Sort_by = input("either input the ID of what you would like to sort by or input 'back' to go back.\n")
        if Sort_by == "back":
            main_menu()
        elif Sort_by == "1" or Sort_by == "2" or Sort_by == "3" or Sort_by == "4":
            break
        else:
            print("")
            print("that is an invalid input")
            print("")

    while True:
        ASC_DESC = input("do you want to sort by ascending or descending? ASC/DESC. type 'back' if you want to go back.\n")
        if ASC_DESC == "back":
            main_menu()
        if ASC_DESC.lower() == "asc" or ASC_DESC.lower() == "desc":
            sql = f"SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID ORDER BY {options[Sort_by]} {ASC_DESC}"
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
            print("")
            db.close()
            break
        else:
            print("")
            print("Invalid input")
            print("")

def show_greaterthan_or_smallerthan():
    options = {"1":"Groceries.price_c",
               "2":"Groceries.Serving_Size_g",
               "3":"Groceries.Calories_Per_Serving",
               "4":"Groceries.Servings"}
    
    options_text = ["| 1. | Price                |",
                    "| 2. | Serving_size         |",
                    "| 3. | Calorise per serving |",
                    "| 4. | Sevings              |"]
    operations = {"1":">",
                  "2":"<"}
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        for option in options_text:
            print(option)
        print("")

        column = input("input the ID of the column you want to sort. If you want to go back to main menu input 'back'.\n")
        if column == "back":
            main_menu()
        elif column == "1" or column == "2" or column == "3" or column == "4":
            break
        else:
            print("")
            print("that is not a valid input")
            print("")
    while True:  
        operator = input("Would you like to sort by greater than or less than?, input 1 or 2. If you want to go back to main menu input 'back'.\n")
        if operator == "back":
            main_menu()
        elif operator == "1" or operator == "2":
            break
        else:
            print("")
            print("that is not a valid input")     
            print("")
    while True:
        try:
            value = int(input("what value would you like to sort by? If you want to go back to main menu input 'back'.\n"))
            if value == "back":
                main_menu()
            sql = f"SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID WHERE {options[str(column)]} {operations[operator]} {value}"
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
            print("")
            print("that is not a valid input")
            print("")

def sort_by_one_brand():
    #show name and id table
    Print_brand_and_ID_for_brands()
    print("")
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run until finished with quere
    while True:
        #try execpt to catch false ID inputs
        try:
            #get users wanted product to show or go back to main menu if wanted
            ID = input("Input the ID of the Brand you would like to sort by about or input 'back' to go back?\n")
            if ID == "back":
                main_menu()
            #run sql quere
            sql = f"SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID WHERE Brand.ID = '{ID}'"
            cursor.execute(sql)
            results = cursor.fetchall()
            #if the ID requested is out of range print invalid id
            if len(results) == 0:
                print("")
                print("Invalid input")
                print("")
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
                print("| Name                                                              | P(c) | SS  | CPS | S  | Type                           | Brand           |")
                print("-"*144)
                for result in results:
                    print(f"| {result[0]:<{Product_Name_Length}} | {result[1]:<{Price_length}} | {result[2]:<{Serving_Size_Length}} | {result[3]:<{Calories_Per_Serving_Length}} | {result[4]:<{Servings_Length}} | {result[5]:<{Product_Type_Length}} | {result[6]:<{Brand_Name_Length}} |")
                print("-"*144)
                print("")
                #stop the function
                db.close()
                break   
        except:
            #if the id inputed wasnt an integer print string:
            print("")
            print("Invalid input")
            print("")

def sort_by_one_product_type():
    #show product_type and ID table
    Print_producttype_and_ID_for_products()
    print("")
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run until finished with quere
    while True:
        #try execpt to catch false ID inputs
        try:
            #get users wanted product to show or go back to main menu if wanted
            ID = input("Input the ID of the Product type you would like to display or input 'back' to go back?\n")
            if ID == "back":
                main_menu()
            #run sql quere
            sql = f"SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID WHERE Product_type.ID = '{ID}'"
            cursor.execute(sql)
            results = cursor.fetchall()
            #if the ID requested is out of range print invalid id
            if len(results) == 0:
                print("")
                print("Invalid input")
                print("")
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
                print("| Name                                                              | P(c) | SS  | CPS | S  | Type                           | Brand           |")
                print("-"*144)
                for result in results:
                    print(f"| {result[0]:<{Product_Name_Length}} | {result[1]:<{Price_length}} | {result[2]:<{Serving_Size_Length}} | {result[3]:<{Calories_Per_Serving_Length}} | {result[4]:<{Servings_Length}} | {result[5]:<{Product_Type_Length}} | {result[6]:<{Brand_Name_Length}} |")
                print("-"*144)
                print("")
                #stop the function
                db.close()
                break   
        except:
            #if the id inputed wasnt an integer print string:
            print("")
            print("Invalid input") 
            print("")

def get_new_data_for_the_table():
    
    while True:
        new_greocery_name = input("what is the name of this new grocery?\n")
        if new_greocery_name == "":
            print("")
            print("Invalid input")
            print("")
        else:
            break
    while True:
        try:
            new_grocery_Calories_per_serving = int(input("how many calories per serving is this new grocey, please don't from using a negitive number.\n"))
            if new_grocery_Calories_per_serving < 0:
                print("")
                print("that is not a positive number try again")
                print("")
            else:
                break
        except:
            print("")
            print("Invalid input")    
            print("")
    while True:
        try:
            new_grocery_servings = int(input("how many servings are in this new grocey, please don't from using a negitive number.\n"))
            if new_grocery_servings < 0:
                print("")
                print("that is not a positive number try again")
                print("")
            else:
                break
        except:
            print("")
            print("Invalid input")    
            print("")
    while True:
        try:
            new_grocery_serving_size_g = int(input("how big are the serving sizes is this new grocey(UNIT grams), please don't from using a negitive number.\n"))
            if new_grocery_serving_size_g < 0:
                print("")
                print("that is not a positive number try again")
                print("")
            else:
                break
        except:
            print("")
            print("Invalid input")    
            print("")
    while True:
        try:
            new_grocery_price_c = int(input("what is the price of this new grocey(UNIT cents), please don't from using a negitive number.\n"))
            if new_grocery_price_c < 0:
                print("")
                print("that is not a positive number try again")
                print("")
            else:
                break
        except:
            print("")
            print("Invalid input")    
            print("")
    Print_brand_and_ID_for_brands()
    found_brand = False
    while True:
        try:
            if found_brand == True:
                break
            new_grocery_brand_name_y_n = input("is your new products brand in this table. y/n\n")
            if new_grocery_brand_name_y_n == "y":
                while True:
                    new_grocery_brand_name = int(input("what is the ID of your products brand name?\n"))
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()
                    sql = "select max(ID) from Product_type"
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    results = results[0]
                    results = results[0]
                    if new_grocery_brand_name in range(1,results):
                        found_brand = True
                        break
                    else:
                        print("Invalid input")
                    db.close()
            elif new_grocery_brand_name_y_n == "n":
                new_grocery_brand_name = input("what is the name of you product's brand?\n")
                break
            else:
                print("")
                print("Invalid input2")
                print("")
        except:
            print("")
            print("Invalid input3")
            print("")
    Print_producttype_and_ID_for_products()
    found_product_type = False
    while True:
        try:
            if found_product_type == True:
                break
            new_grocery_product_type_y_n = input("is your new products brand in this table. y/n\n")
            if new_grocery_product_type_y_n == "y":
                while True:
                    new_grocery_product_type = int(input("what is the ID of your products brand name?\n"))
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()
                    sql = "select max(ID) from Brand"
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    results = results[0]
                    results = results[0]
                    if new_grocery_product_type in range(1,results):
                        found_product_type = True
                        break
                    else:
                        print("Invalid input")
                    db.close()
            elif new_grocery_product_type_y_n == "n":
                new_grocery_product_type = input("what is the name of you product's brand?\n")
                break
            else:
                print("")
                print("Invalid input2")
                print("")

        except:
            print("")
            print("Invalid input3")
            print("")


            


def main_menu():
    while True:
        all_options = {"1":search_for_grocery,
                       "2":ORDER_BY,
                       "3":show_greaterthan_or_smallerthan,
                       "4":sort_by_one_brand,
                       "5":sort_by_one_product_type,
                       "6":print_whole_table,
                       "7":get_new_data_for_the_table}
        all_options_text = ["| 1.    | Search for a specific item                        |",
                            "| 2.    | sort by a specific data type                      |",
                            "| 3.    | sort any column by greater than or smaller than   |",
                            "| 4.    | search for all items with a specific brand        |",
                            "| 5.    | search for all items with a specific product type |",
                            "| 6.    | print the whole table                             |",
                            "| 7.    | add data to the table                             |",
                            "| quit. | Quit the program                                  |"]
        for option in all_options_text:
            print(option)
        try:
            option_chosen = input("what would you like to do?\n") 
            if str(option_chosen) in all_options:    
                all_options[option_chosen]()
            elif str(option_chosen).lower() ==  "quit." or str(option_chosen).lower() == "quit":
                break
            else:
                print("")
                print("that is not an option") 
                print("") 
        except:
            print("")
            print("that is not an option")
            print("")


main_menu()
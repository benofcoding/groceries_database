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

username_count = 5
password_count = 5
#all functions



def print_whole_table():
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run sql quere
    sql = "SELECT Groceries.ID, Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID"
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
    print("| ID | Name                                                              | P(c) | SS  | CPS | S  | Type                      | Brand           |")
    print("-"*144)
    for result in results:
        print(f"| {result[0]:<{Product_ID_Length}} | {result[1]:<{Product_Name_Length}} | {result[2]:<{Price_length}} | {result[3]:<{Serving_Size_Length}} | {result[4]:<{Calories_Per_Serving_Length}} | {result[5]:<{Servings_Length}} | {result[6]:<{Product_Type_Length}} | {result[7]:<{Brand_Name_Length}} |")
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
    sql = "SELECT Groceries.ID, Groceries.Name FROM Groceries ORDER BY groceries.ID ASC"
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
                main_menu(login)
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
            main_menu(login)
        elif Sort_by == "1" or Sort_by == "2" or Sort_by == "3" or Sort_by == "4":
            break
        else:
            print("")
            print("that is an invalid input")
            print("")

    while True:
        ASC_DESC = input("do you want to sort by ascending or descending? ASC/DESC. type 'back' if you want to go back.\n")
        if ASC_DESC == "back":
            main_menu(login)
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
            main_menu(login)
        elif column == "1" or column == "2" or column == "3" or column == "4":
            break
        else:
            print("")
            print("that is not a valid input")
            print("")
    while True:  
        operator = input("Would you like to sort by greater than or less than?, input 1 or 2. If you want to go back to main menu input 'back'.\n")
        if operator == "back":
            main_menu(login)
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
                main_menu(login)
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
                main_menu(login)
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
                main_menu(login)
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

def gets_new_data_for_the_table_and_appends_all_new_data():
    
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
    new_brand = False
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
                    if new_grocery_brand_name in range(1,results+1):

                        found_brand = True
                        break
                    else:
                        print("Invalid input")
                    db.close()
            elif new_grocery_brand_name_y_n == "n":
                new_brand = True
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
    new_product_type = False
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
                    if new_grocery_product_type in range(1,results+1):
                        found_product_type = True

                        break
                    else:
                        print("Invalid input")
                    db.close()
            elif new_grocery_product_type_y_n == "n":
                new_product_type = True
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

    while True:
        try:
            you_sure = input("are you sure you want to append this data? y/n\n")
            if you_sure == "y":
                if new_brand == True:
                    append_data_to_brand_table(new_grocery_brand_name)
                if new_product_type == True:
                    append_data_to_product_type_table(new_grocery_product_type)

                new_brand_ID = get_id_for_new_brand(new_grocery_brand_name, new_grocery_brand_name)

                new_product_type_ID = get_id_for_new_product_type(new_grocery_product_type, new_grocery_product_type)

                print(new_brand_ID)
                print(new_product_type_ID)
                append_data_to_the_grocery_table(new_greocery_name, new_grocery_servings, new_grocery_serving_size_g, new_grocery_price_c, new_grocery_Calories_per_serving, new_brand_ID, new_product_type_ID)
                break
            elif you_sure == "n":
                main_menu(login)
            else:
                print("Invalid input")
        except:
            print("invalid")

def append_data_to_brand_table(brand):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"insert into brand (Name) select '{brand}'"
    cursor.execute(sql)
    db.commit()
    db.close()

def append_data_to_product_type_table(product_type):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"insert into Product_type (Type) select '{product_type}'"
    cursor.execute(sql)
    db.commit()
    db.close()

def get_id_for_new_brand(new_brand_id, new_brand_name):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    try:
        sql = f"select brand.ID from brand where brand.ID = {new_brand_id}"
        cursor.execute(sql)
    except:
        try:
            sql = f"select brand.ID from brand where brand.Name = '{new_brand_name}'"
            cursor.execute(sql)
        except:
            pass
    results = cursor.fetchall()
    results = results[0]
    results = results[0]
    return results

def get_id_for_new_product_type(new_product_type_id, new_product_type):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    try:
        sql = f"select product_type.ID from product_type where product_type.ID = {new_product_type_id}"
        cursor.execute(sql)
    except:
        try:
            sql = f"select product_type.ID from product_type where product_type.type = '{new_product_type}'"
            cursor.execute(sql)
        except:
            pass
    results = cursor.fetchall()
    results = results[0]
    results = results[0]
    return results

def append_data_to_the_grocery_table(grocery_name, grocery_servings, grocery_serving_size, grocery_price, grocery_cps, brand_id, product_type_id):
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = f"insert into groceries (name, brand_id, calories_per_serving, servings, serving_size_g, price_c, product_type_id) select '{grocery_name}', {brand_id}, {grocery_cps}, {grocery_servings}, {grocery_serving_size}, {grocery_price}, {product_type_id}"
    cursor.execute(sql)
    db.commit()
    db.close()

def username_and_password(count_username, count_password):
    print("before we start we need username an password for some of the database editing options")
    username = "Ben Gorman"
    password = "password1234"
    while count_username != 0:
        username_input = input("what is your username")
        if username_input == username:
            break
        else:
            count_username -= 1
            print("")
            print(f"invalid username you have {count_username} more attempts")
            print("")
    
    if count_username == 0:
        print("")
        print("you are out of username attempts")
        print("")
        return "failed"

    while count_password != 0:
        password_input = input("what is your password")
        if password_input == password:
            return "success"
        else:
            count_password -= 1
            print("")
            print(f"invalid password you have {count_password} more attempts")
            print("")
            
    if count_password == 0:
        print("")
        print("you are out of username attempts")
        print("")
        return "failed"

def remove_data_from_groceries_table():
    print_whole_table()
    while True:
        try:
            remove_id = int(input("input the id of the grocery you would like to remove.\n"))
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            sql = "select max(ID) from groceries"
            cursor.execute(sql)
            results = cursor.fetchall()
            results = results[0]
            results = results[0]
            print(results)
            if remove_id in range(1,results+1):
                db = sqlite3.connect(DATABASE)
                cursor = db.cursor()
                sql = f"delete from Groceries where ID = {remove_id}"
                cursor.execute(sql)
                db.commit()
                db.close
                break
            else:
                print("")
                print("Invalid input")
                print("")
            db.close
        except:
            print("")
            print("Invalid input")
            print("")



def main_menu(password_check):
    while True:
        all_options = {"1":search_for_grocery,
                       "2":ORDER_BY,
                       "3":show_greaterthan_or_smallerthan,
                       "4":sort_by_one_brand,
                       "5":sort_by_one_product_type,
                       "6":print_whole_table,
                       "7":gets_new_data_for_the_table_and_appends_all_new_data,
                       "8":remove_data_from_groceries_table}
        blocked_options = ["8"]
        all_options_text = ["| 1.    | Search for a specific item                        |",
                            "| 2.    | sort by a specific data type                      |",
                            "| 3.    | sort any column by greater than or smaller than   |",
                            "| 4.    | search for all items with a specific brand        |",
                            "| 5.    | search for all items with a specific product type |",
                            "| 6.    | print the whole table                             |",
                            "| 7.    | add data to the table                             |",
                            "| 8.    | remove a piece of data from the groceries table   |",
                            "| quit. | Quit the program                                  |"]
        for option in all_options_text:
            print(option)
        try:
            option_chosen = input("what would you like to do?\n") 
            if str(option_chosen) in all_options: 
                if (str(option_chosen) in blocked_options):
                    if password_check == "failed":
                        print("this option is blocked as you have failed to input a correct username or password")
                    else:
                        all_options[option_chosen]()
                else:
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

login = username_and_password(username_count, password_count)

main_menu(login)
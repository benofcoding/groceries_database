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

username_count = 5
password_count = 5


#all functions
def print_whole_table():
    """this function prints the whole table including: ID, Name, price, calorise per serving,
    servings, servings size, brand name, product type"""
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run sql quere
    sql = "SELECT Groceries.ID, Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID"
    cursor.execute(sql)
    results = cursor.fetchall()
    #print the acronyms key for column names
    Acronmys = ["P(c) = Price in cents",
                "SS = Servin size in grams",
                "CPS = Calories per serving",
                "S = servings"]
    print("")
    #print nicely
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
    """this function prints the product type ID and product type"""
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
    """this function prints the Grocery name and Grocery ID"""
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
    """this function print the Brand name and Brand ID"""
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
    """this function lets the user input the ID of a specific grocery and it will
    bring up more information about that specific Grocery."""
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
    """this function lets the user sort one of the columns[price, servings size, servings, calories per person]
    be either ascending or descending"""
    #options for the user to choose
    options = {"1":"Groceries.price_c",
                        "2":"Groceries.Serving_Size_g",
                        "3":"Groceries.Calories_Per_Serving",
                        "4":"Groceries.Servings"}
    #list of options to print them nicely
    options_text = ["| 1. | Price                |",
                    "| 2. | Serving_size         |",
                    "| 3. | Calorise per serving |",
                    "| 4. | Sevings              |"]
    #prints the options nicely
    for option in options_text:
        print(option)
    print("")

    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #runs until it gets a valid input for the sort column options
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

    #runs untile the function is successful
    while True:
        #gets the user input for ASC or DESC
        ASC_DESC = input("do you want to sort by ascending or descending? ASC/DESC. type 'back' if you want to go back.\n")
        #checks to see if the user wants to go back to the main menu
        if ASC_DESC == "back":
            main_menu(login)
        #checks to see if the user inputed correctly
        if ASC_DESC.lower() == "asc" or ASC_DESC.lower() == "desc":
            #runs correct sql quere based of the inputs
            sql = f"SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID ORDER BY {options[Sort_by]} {ASC_DESC}"
            cursor.execute(sql)
            results = cursor.fetchall()
            
            #print the acronyms key for column names  
            Acronmys = ["P(c) = Price in cents",
                        "SS = Servin size in grams",
                        "CPS = Calories per serving",
                        "S = servings"]
            print("")
            #prints nicely
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
        #if the input was incorrect prints:
        else:
            print("")
            print("Invalid input")
            print("")

def show_greaterthan_or_smallerthan():
    """this funtion lets the user filter any column[price, servings size, servings, calories per person]
    by greater than or less than by an inputed value"""
    #options for the user to choose
    options = {"1":"Groceries.price_c",
               "2":"Groceries.Serving_Size_g",
               "3":"Groceries.Calories_Per_Serving",
               "4":"Groceries.Servings"}
    #list of options to print them nicely
    options_text = ["| 1. | Price                |",
                    "| 2. | Serving_size         |",
                    "| 3. | Calorise per serving |",
                    "| 4. | Sevings              |"]
    #list of operations the user can choose
    operations = {"1":">",
                  "2":"<"}
    
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    #runs until gets a correct input for column
    while True:
        #prints all the columns nicely
        for option in options_text:
            print(option)
        print("")
        #asks for column input
        column = input("input the ID of the column you want to sort. If you want to go back to main menu input 'back'.\n")
        #checks to see if user wants to go back to main menu
        if column == "back":
            main_menu(login)
        #checks to see if user inputed correct column name
        elif column == "1" or column == "2" or column == "3" or column == "4":
            break
        #if the user inputed incorrect column name print:
        else:
            print("")
            print("that is not a valid input")
            print("")
    #runs until correct operation inputed
    while True:  
        #asks user for operation to filter by
        operator = input("Would you like to sort by greater than or less than?, input 1 or 2. If you want to go back to main menu input 'back'.\n")
        #checks to see if user wants to go back to main menu
        if operator == "back":
            main_menu(login)
        #checks to see if user inputed correct operation
        elif operator == "1" or operator == "2":
            break
        #if inputed invalid operation print:
        else:
            print("")
            print("that is not a valid input")     
            print("")
    #runs until the function is finished
    while True:
        try:
            #asks for value user wants to filter by
            value = int(input("what value would you like to sort by? If you want to go back to main menu input 'back'.\n"))
            #checks to see if user wants to go back to menu
            if value == "back":
                main_menu(login)
            #runs correct sql quere based of given inputs
            sql = f"SELECT Groceries.Name, Groceries.price_c, Groceries.Serving_Size_g, Groceries.Calories_Per_Serving, Groceries.Servings, Product_Type.Type, Brand.Name FROM Groceries JOIN Brand on Brand.ID = Groceries.Brand_ID JOIN Product_Type on Product_Type.ID = Groceries.Product_Type_ID WHERE {options[str(column)]} {operations[operator]} {value}"
            cursor.execute(sql)
            results = cursor.fetchall()
            print(options[str(column)])
            #prints the acroynms for the column names
            Acronmys = ["P(c) = Price in cents",
                        "SS = Servin size in grams",
                        "CPS = Calories per serving",
                        "S = servings"]
            print("")
            #prints data nicely
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
        #if int input was invalid print:
        except:
            print("")
            print("that is not a valid input")
            print("")

def sort_by_one_brand():
    """this funtion lets the user filter by any inputed brand"""
    #show brand and id table
    Print_brand_and_ID_for_brands()
    print("")
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run until finished with quere
    while True:
        #try execpt to catch false ID inputs
        try:
            #get users wanted brand to sort by or go back to main menu if wanted
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
    """this function lets the user filter by any specific product type"""
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
    """this function gets all the inputs for appending new data to all of the tables from the user"""
    #runs until it gets a valid new grocery name
    while True:
        new_greocery_name = input("what is the name of this new grocery?\n")
        #checks to see if grocery name is invalid
        if new_greocery_name == "":
            print("")
            print("Invalid input")
            print("")
            #if grocery name is valid then breaks and moves on
        else:
            break
    #runs until it gets a valid new calories per serving
    while True:
        try:
            new_grocery_Calories_per_serving = int(input("how many calories per serving is this new grocey, please don't from using a negitive number.\n"))
            #checks to see if calories per serving is invalid
            if new_grocery_Calories_per_serving < 0:
                print("")
                print("that is not a positive number try again")
                print("")
            #if calories per serving is valid then breaks and moves on
            else:
                break
        except:
            print("")
            print("Invalid input")    
            print("")
    #runs until it gets a valid new servings
    while True:
        try:
            new_grocery_servings = int(input("how many servings are in this new grocey, please don't from using a negitive number.\n"))
            #checks to see if servings is invalid
            if new_grocery_servings < 0:
                print("")
                print("that is not a positive number try again")
                print("")
            #if servins is valid then breaks and moves on
            else:
                break
        except:
            print("")
            print("Invalid input")    
            print("")
    #runs until it gets a valid new serving size
    while True:
        try:
            new_grocery_serving_size_g = int(input("how big are the serving sizes is this new grocey(UNIT grams), please don't from using a negitive number.\n"))
            #checks to see if serving size is invalid
            if new_grocery_serving_size_g < 0:
                print("")
                print("that is not a positive number try again")
                print("")
            #if serving size is valid then breaks and moves on
            else:
                break
        except:
            print("")
            print("Invalid input")    
            print("")
    #runs until it gets a valid new price
    while True:
        try:
            new_grocery_price_c = int(input("what is the price of this new grocey(UNIT cents), please don't from using a negitive number.\n"))
            #checks to see if price is invalid
            if new_grocery_price_c < 0:
                print("")
                print("that is not a positive number try again")
                print("")
            #if price is valid then breaks and moves on
            else:
                break
        except:
            print("")
            print("Invalid input")    
            print("")
    #prints the table forbrand and ID
    Print_brand_and_ID_for_brands()
    new_brand = False
    found_brand = False
    while True:
        try:
            #breaks when found brand
            if found_brand == True:
                break
            #asks if user new brand in the table or not
            new_grocery_brand_name_y_n = input("is your new products brand in this table. y/n\n")
            #if it is then:
            if new_grocery_brand_name_y_n == "y":
                #runs until user inputs valid brand id
                while True:
                    #asks what the ID of users brand is
                    new_grocery_brand_name = int(input("what is the ID of your products brand name?\n"))
                    #establish interface
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()
                    #run sql quere
                    sql = "select ID from Brand"
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    #makes list and appends all brands
                    all_brand_ids = []
                    for IDs in results:
                        all_brand_ids.append(IDs[0])
                    db.close
                    #checks to see if users inputed brands is valid
                    if new_grocery_brand_name in all_brand_ids:
                        #breaks and tells outside while loop to break if valid ID
                        found_brand = True
                        break
                    else:
                        #if invalid id print :
                        print("Invalid input")
                    db.close()
            #if users wanted brand not in table:
            elif new_grocery_brand_name_y_n == "n":
                #asks for the name of new brand then breaks
                #also sets new brand variable to true
                new_brand = True
                new_grocery_brand_name = input("what is the name of you product's brand?\n")
                break
        #if anything was invalid does:
            else:
                print("")
                print("Invalid input")
                print("")
        except:
            print("")
            print("Invalid input")
            print("")

    #this whole next section is the exact same as the section above for brand but for product type
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
                    sql = "select ID from product_type"
                    cursor.execute(sql)
                    results = cursor.fetchall()
                    all_product_type_ids = []
                    for IDs in results:
                        all_product_type_ids.append(IDs[0])
                    db.close
                    if new_grocery_product_type in all_product_type_ids:
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
                print("Invalid input")
                print("")

        except:
            print("")
            print("Invalid input")
            print("")

    #runs until appended all of the new data
    while True:
        try:
            #asks for confermation to append data
            you_sure = input("are you sure you want to append this data? y/n\n")
            #if user says yes then:
            if you_sure == "y":
                #if the user has a new brand then it appends the name and a new id to the brand table
                if new_brand == True:
                    append_data_to_brand_table(new_grocery_brand_name)
                #if the user has a new product type then it appends the type and a new id to the product type table
                if new_product_type == True:
                    append_data_to_product_type_table(new_grocery_product_type)
                #gets the ID of the new brand based on ID or name
                new_brand_ID = get_id_for_new_brand(new_grocery_brand_name, new_grocery_brand_name)
                #gets the ID of the new product type based of ID or type
                new_product_type_ID = get_id_for_new_product_type(new_grocery_product_type, new_grocery_product_type)
                #appends all of the new data to the grocery table
                append_data_to_the_grocery_table(new_greocery_name, new_grocery_servings, new_grocery_serving_size_g, new_grocery_price_c, new_grocery_Calories_per_serving, new_brand_ID, new_product_type_ID)
                break
            #if user says no then goes to main menu
            elif you_sure == "n":
                main_menu(login)
            #if user was invalid then:
            else:
                print("Invalid input")
        except:
            print("invalid")

def append_data_to_brand_table(brand):
    """this function appends data to the brand table based on a given input to the function"""
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run sql query
    sql = f"insert into brand (Name) select '{brand}'"
    cursor.execute(sql)
    db.commit()
    db.close()

def append_data_to_product_type_table(product_type):
    """this function appends data to the product type table based on a given input to the function"""
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run sql query
    sql = f"insert into Product_type (Type) select '{product_type}'"
    cursor.execute(sql)
    db.commit()
    db.close()

def get_id_for_new_brand(new_brand_id, new_brand_name):
    """this function returns the ID of a given name or ID from the brand table"""
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #trys to find the ID based of of the given information,
    #if the input was id then it finds it in the first sql line
    #if the input was a name then the second sql line with find the ID
    try:
        sql = f"select brand.ID from brand where brand.ID = {new_brand_id}"
        cursor.execute(sql)
    except:
        try:
            sql = f"select brand.ID from brand where brand.Name = '{new_brand_name}'"
            cursor.execute(sql)
        except:
            pass
    #gets the id in nice format
    results = cursor.fetchall()
    results = results[0]
    results = results[0]
    #returns the ID of the brand
    return results

def get_id_for_new_product_type(new_product_type_id, new_product_type):
    """this function returns the ID of a given type or ID from the product type table"""
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #trys to find the ID based of of the given information,
    #if the input was id then it finds it in the first sql line
    #if the input was a type then the second sql line with find the ID
    try:
        sql = f"select product_type.ID from product_type where product_type.ID = {new_product_type_id}"
        cursor.execute(sql)
    except:
        try:
            sql = f"select product_type.ID from product_type where product_type.type = '{new_product_type}'"
            cursor.execute(sql)
        except:
            pass
    #gets the ID in a nice format
    results = cursor.fetchall()
    results = results[0]
    results = results[0]
    #returns the ID of the type
    return results

def append_data_to_the_grocery_table(grocery_name, grocery_servings, grocery_serving_size, grocery_price, grocery_cps, brand_id, product_type_id):
    """this function appends data inputed to the grocery table"""
    #establish interface
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #run sql query with all of the given new data
    sql = f"insert into groceries (name, brand_id, calories_per_serving, servings, serving_size_g, price_c, product_type_id) select '{grocery_name}', {brand_id}, {grocery_cps}, {grocery_servings}, {grocery_serving_size}, {grocery_price}, {product_type_id}"
    cursor.execute(sql)
    db.commit()
    db.close()

def username_and_password(count_username, count_password):
    """this funciton gets the user to input a username and password and returs either 'falied' or 'success' based on the inputs"""
    print("")
    print("before we start we need username an password for some of the database editing options")
    print("")
    #constants
    username = "ben gorman"
    password = "password1234"
    #runs until out of atempts for correct username
    while count_username != 0:
        #asks for username input
        username_input = input("What is your username? if you want to continue without logging in say 'main menu'\n")
        print("")
        #checks to see if username is correct
        #if so return success
        #if the username is false returns failed and takes one of the count
        #if the user decided not to log in then returns failed
        if username_input.lower() == username:
            return "success"
        elif username_input.lower() == "main menu":
            return "failed"
        else:
            count_username -= 1
            print("")
            print(f"invalid username you have {count_username} more attempts")
            print("")
    
    #checks to see if the username count reached zero:
    #if so then returns failed
    if count_username == 0:
        print("")
        print("you are out of username attempts")
        print("")
        return "failed"

    #runs until out of atempts for correct password
    while count_password != 0:
        #asks for password input
        password_input = input("What is your password? if you want to continue without logging in say 'main menu'\n")
        #checks to see if password is correct
        #if so return success
        #if the password is false returns failed and takes one of the count
        #if the user decided not to log in then returns failed
        if password_input == password:
            return "success"
        elif username_input.lower() == "main menu":
            return "failed"
        else:
            count_password -= 1
            print("")
            print(f"invalid password you have {count_password} more attempts")
            print("")
    
    #checks to see if the password count reached zero:
    #if so then returns failed
    if count_password == 0:
        print("")
        print("you are out of username attempts")
        print("")
        return "failed"

def remove_data_from_groceries_table():
    """this function removes data from the grocery table based on the given input"""
    #prints the whole table
    print_whole_table()
    while True:
        try:
            #asks for the ID if the grocery you want to remove
            remove_id = int(input("input the id of the grocery you would like to remove.\n"))
            #establish interface
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            #run sql query
            sql = "select ID from groceries"
            cursor.execute(sql)
            results = cursor.fetchall()
            #makes a list and appends all grocery ID's
            all_grocery_ids = []
            for IDs in results:
                all_grocery_ids.append(IDs[0])
            db.close
            #checks to see if given id was in real ids list
            #if so then removes data from grocery table
            if remove_id in all_grocery_ids:
                #establish interface
                db = sqlite3.connect(DATABASE)
                cursor = db.cursor()
                #run sql query
                sql = f"delete from Groceries where ID = {remove_id}"
                cursor.execute(sql)
                db.commit()
                db.close
                break
        #if anything breaks then:
            else:
                print("")
                print("Invalid input")
                print("")
            db.close
        except:
            print("")
            print("Invalid input")
            print("")

def remove_data_from_brand_table():
    """this function gets the user to input the ID of the brand they would like to remove and removes it.
    it also removes all coresponding grocerys with that brand"""
    #runs until function over
    while True:
        try:
            #prints brand table
            Print_brand_and_ID_for_brands()
            print("")
            #asks for the brand ID you want to remove
            remove_brand_id = int(input("what is the ID of the brand you would like to remove?\n"))
            print("")
            #establish interface
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            #runs sql query to find all brand ID's
            sql = "select ID from Brand"
            cursor.execute(sql)
            results = cursor.fetchall()
            #makes a list and appends all brand ID's to the list
            all_brand_ids = []
            for IDs in results:
                all_brand_ids.append(IDs[0])
            db.close

            #verify's that user inputed valid ID in real ids list
            if remove_brand_id in all_brand_ids:
                #asks for confermation because removing brands will sometimes also remove grocerys
                print("")
                confirm = input("are you sure you want to delete that brand y/n WARNING if you delete a brand that a grocery has set as its ID it will be deleted\n")
                print("")
                #if confirmation was yes then remove brand from brand table and any corosponding grocerys with that brand from grocery table
                if confirm == "y":
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()
                    sql = f"delete from groceries where Brand_id = {remove_brand_id}"
                    cursor.execute(sql)
                    db.commit()
                    sql = f"delete from brand where ID = {remove_brand_id}"
                    cursor.execute(sql)
                    db.commit()
                    db.close
                    break
                #if confirmation is no then go to main menu
                if confirm == "n":
                    main_menu()

        #if anything breaks:
            else:
                print("")
                print("invalid input")
                print("")
        except:
            print("")
            print("invalid input")
            print("")

def remove_data_from_product_type_table():
    """this function gets the user to input the ID of the product_type they would like to remove and removes it.
    it also removes all coresponding grocerys with that product_type"""
    #runs until function over
    while True:
        try:
            #prints product type table
            Print_producttype_and_ID_for_products()
            print("")
            #asks for the product type ID you want to remove
            remove_product_type_id = int(input("what is the ID of the producttype you would like to remove?\n"))
            print("")
            #establish interface
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            #runs sql query to find all product type ID's
            sql = "select ID from Product_type"
            cursor.execute(sql)
            results = cursor.fetchall()
            #makes a list and appends all product type ID's to the list
            all_product_type_ids = []
            for IDs in results:
                all_product_type_ids.append(IDs[0])
            db.close
            #verify's that user inputed valid ID in real ids list
            if remove_product_type_id in all_product_type_ids:
                #asks for confermation because removing product type will sometimes also remove grocerys
                print("")
                confirm = input("are you sure you want to delete that product type y/n WARNING if you delete a product type that a grocery has set as its ID it will be deleted\n")
                print("")
                #if confirmation was yes then remove product type from product type table and any corosponding grocerys with that product type from grocery table
                if confirm == "y":
                    db = sqlite3.connect(DATABASE)
                    cursor = db.cursor()
                    sql = f"delete from groceries where Product_type_id = {remove_product_type_id}"
                    cursor.execute(sql)
                    db.commit()
                    sql = f"delete from product_type where ID = {remove_product_type_id}"
                    cursor.execute(sql)
                    db.commit()
                    db.close
                    break
                #if confirmation is no then go to main menu
                if confirm == "n":
                    main_menu()
        #if anything above had an incorrect input then:
            else:
                print("")
                print("invalid input")
                print("")
        except:
            print("")
            print("invalid input")
            print("")

def main_menu(password_check):
    """this function controls the useage of all of the other functions that the user can use. 
    it gets the user to input the ID of the function they want to use. if required it checks that the user
    has successfully logged in with a password. it also lets you quit the program"""
    #runs until function over
    while True:
        #dictionary of every functon the user can run with a coresopding key
        all_options = {"1":search_for_grocery,
                       "2":ORDER_BY,
                       "3":show_greaterthan_or_smallerthan,
                       "4":sort_by_one_brand,
                       "5":sort_by_one_product_type,
                       "6":print_whole_table,
                       "7":gets_new_data_for_the_table_and_appends_all_new_data,
                       "8":remove_data_from_groceries_table,
                       "9":remove_data_from_brand_table,
                       "10":remove_data_from_product_type_table}
        #list of all the password protected functions
        blocked_options = ["7", "8", "9", "10"]
        #list of the lines that the main menu needs to print to look nice
        all_options_text = ["| 1.    | Search for a specific item                         |",
                            "| 2.    | sort by a specific data type                       |",
                            "| 3.    | sort any column by greater than or smaller than    |",
                            "| 4.    | search for all items with a specific brand         |",
                            "| 5.    | search for all items with a specific product type  |",
                            "| 6.    | print the whole table                              |",
                            "| 7.    | add data to the database                           |",
                            "| 8.    | remove a piece of data from the groceries table    |",
                            "| 9.    | remove a piece of data from the brand table        |",
                            "| 10.   | remove a piece of data from the product type table |",
                            "| quit. | Quit the program                                   |"]
        #prints options nicely
        for option in all_options_text:
            print(option)
        try:
            #asks the user what they would like to do
            option_chosen = input("what would you like to do?\n") 
            #checks to see if option choosen is in the dictionary
            if str(option_chosen) in all_options: 
                #checks to see if the option choosen is a password protected option
                if (str(option_chosen) in blocked_options):
                    #checks to see if the password check has been failed before
                    if password_check == "failed":
                        #if it has then prints:
                        print("")
                        print("this option is blocked as you have failed to input a correct username or password")
                        print("")
                    #if it hasn't then runs function:
                    else:
                        all_options[option_chosen]()
                #if it isn't then runs function:
                else:
                    all_options[option_chosen]()
            #checks to see if the user wanted to quit
            elif str(option_chosen).lower() ==  "quit." or str(option_chosen).lower() == "quit":
                break
        #if the user input was invalid then:
            else:
                print("")
                print("that is not an option") 
                print("") 
        except:
            print("")
            print("that is not an option")
            print("")


#runs the login at the start using the count variables in constants
login = username_and_password(username_count, password_count)

#runs main menu to get started
main_menu(login)
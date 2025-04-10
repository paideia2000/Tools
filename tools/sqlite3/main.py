import re
from mysql.connector import  Error
from package_poo.Querys import CreateTableQuery, SelectQuery, InsertQuery, UpdateQuery, DeleteQuery
from package_poo.GetConnection import ConnectionPool

def get_data_CREATETABLE() -> str:
    """ execute query create table """
    try:
        while True:
            name_table = input("\nPlease insert the name table: ").strip().lower()#get table name
            
            if re.search(r'\b[A-Za-z]{2,}\b', name_table):
                return name_table
            else:
                print(f"\n¡ERROR!: The table name '{name_table}' can only have alphabetical letters.")

    except Exception as ex:
        raise ex

def get_data_INSERT() -> tuple:
    """ execute the option three that is insert users data to the database """
    try:
        while True:#valid name user
            get_name = input("\nEnter the user name: ").strip().lower()
            if re.fullmatch(r'[A-Za-z]+',get_name):
                print("CORRECT.")
                break
            else:
                print("¡ERROR! Check the fiel")
        while True:#valid age user
            get_age = input("\nEnter the age: ")
            if get_age.isdigit():
                if 14 <= int(get_age) <= 90:
                    print("CORRECT")
                    break
                else:
                    print("ERROR The age must be between 14 and 90 years old.")
            else:
                print("¡ERROR! Check the fiel. The age musb be a integer number.")
        while True:#valid country user
            get_country = input("\nEnter the country: ").strip().lower()
            if re.fullmatch(r'[A-Za-z]+',get_country):
                print("CORRECT.")

                break
            else:
                print("¡ERROR! Please chek the field tha are not correct.")
        while True:#valid email user
            get_email = input("\nEnter the email: ").strip()
            if re.search(r'^[A-Za-z0-9#$%&]+@[A-Za-z0-9$%&#]+\.[a-z]{2,}\b',get_email):
                print("CORRECT.")
                break
            else: 
                print("¡ERROR! Please chek the field tha are not correct.")

        data_users = (get_name, get_age, get_country, get_email,)
        return data_users
    
    except Exception as ex:
        raise ex

def get_data_UPDATE(COLUMN) -> str | tuple:
    """ execute the option 3 that is update users data to the database """
    
    
    try:
        while True:
            name_column = input("\nEnter the column name: ").strip().lower()
            if name_column in COLUMN:
                print("CORRECT")
                break
            else:
                print(f"The name '{name_column}' dosen't existis.")
        while True:
            new_value = input("\nEnter the new value: ").strip().lower()
            if re.search(r'[A-Za-z0-9"#$%&]',new_value):
                print("CORRECT")
                break
            else:
                print(f"The value '{new_value}' is incorrect")
        while True:
            user_id = input("\nEnter the ID of the user you want to make the modification to: ")
            if user_id.isdigit() >= 1:
                print("CORRECT")
                break
            else:
                print(f"The value '{user_id}' is incorrect")
            
        new_data = (new_value,user_id)
        
        if isinstance(new_data, tuple) and name_column:
            return name_column, new_data
        else:
            raise ValueError("Some of the data is invalid")
            
    except Exception as exp:
        print(f"\nAn error ocurred: {exp}\n")

def get_data_DELETE() -> str | int:
    """ execute the option 4 that is delete users to the database """
    try:

        while True:
            name_table = input("\nEnter the table name: ").strip().lower()
            if re.fullmatch(r'[A-Za-z]+',name_table):
                print("CORRECT")
                break
            else:
                print(f"The value '{name_table}' dosen't exists.")
        while True:
            user_id = input("\nEnter the ID of the user you want to make the modification to: ")
            if user_id.isdigit() >= 1:
                print("CORRECT")
                break
            else:
                print(f"The value '{user_id}' is incorrect")
            
        if name_table and user_id:
            return name_table, int(user_id)
        else:
            raise ValueError("Some of the data is invalid. Please try again.")

    except Error:
            print(f"\nError the table with the name '{name_table}' dosen't exists.")

    except Exception as ex:
        print(f"An error ocurred: {ex}")

def get_data_SELECT(COLUMN) -> str:
    """ execute the query select  """

    while True:
        try:
            name_table: str = input("\nInserte the name table ->: ").strip().lower()
            name_colums: str = input("Inserte the name of the columns ->: ").strip().lower()
            
            if re.fullmatch(r'[A-Za-z]+', name_table) and name_colums in COLUMN:
                return name_table, name_colums
            else:
                print(f"\n¡ERROR! The column named '{name_colums}' does not exist")
        
        except Exception as ex :
            raise ex

def get_choise_admin(PROMPT: str, conex: callable, COLUMNS: list[str]) -> None:
    """ get the option of the user want execute """
    while True:
        try:
            number: int = int(input(PROMPT))
            if number == 1:
                name_table: str = get_data_CREATETABLE()
                create = CreateTableQuery()#object created from the module 'Querys' froom the class 'CreateTableQuery'
                create.execute_query(conex.connection(), name_table)#call the method 'execute_query' of the class 'CreateTableQuery'
                break
                
            if number == 2:
                data_user: tuple = get_data_INSERT()
                insert: object = InsertQuery()#object create from the module 'Querys' froom the class 'InsertQuery'
                insert.execute_query(conex.connection(), data_user)#call the method of the class 'InsertQuery'
                break
                
            if number == 3:
                name_column, new_data_user = get_data_UPDATE(COLUMNS)
                update =UpdateQuery()
                update.execute_query(conex.connection(), name_column, new_data_user)
                break
            
            if number == 4:
                name_tabl, user_id = get_data_DELETE()
                delete = DeleteQuery()#object create from the module 'Querys' froom the class 'DeletetQuery'
                delete.execute_query(conex.connection(), name_tabl, int(user_id))#call the method of the class 'DeleteQuery'
                break
            
            if number == 5:
                name_table, filter_by = get_data_SELECT(COLUMNS)
                
                select: object = SelectQuery()#object created from the module 'Querys' froom the class 'SelectQuery'
                select.execute_query(conex.connection(), filter_by, name_table)#call the method of the class 'SelectQuery'
                break

        except ValueError:
            print("\n¡ERROR! You need into a integer value. Please try again.")
        except Exception as exp:
            print(f"\nAn error ocurred: {exp}")

def interface_user() -> None:
    """ Interface of the users """
    print("WLECOME TO THE DATABASE MANAGER".center(100))
    print("\nChoise the option (1) for CREATE table.","\nChoise the option (2) for INSERT the users data to the database.",
        "\nChoise the option (3) for UPDATE the users data to the database.","\nChoise the option (4) for DELETE data fron the table.",
        "\nChoise the option (5) for SELECT data fron the table.")

def main():
    
    COLUMNS = ["id", "name", "email", "country", "age", "*", "city"]
    conex: object = ConnectionPool("localhost", "root", "Derrickrose1?", "users")#objet oh the class Connection that stablish connection with the pool connection
    
    interface_user()#show the user interface
    get_choise_admin("\nWhich option do you want to perform: ", conex, COLUMNS)

if __name__=="__main__":
    main()

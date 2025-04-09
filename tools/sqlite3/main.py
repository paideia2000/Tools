import re
from package_poo import Querys
from package_poo.GetConnection import Connection

def execute_choise_1(conex: callable) -> None:
    """ execute query create table """
    try:
        while True:
            name_table = input("\nPlease insert the name table: ").strip().lower()#get table name

            if re.search(r'\b[A-Za-z]{2,}\b', name_table):
                create = Querys.CreateTableQuery()
                create.execute_query(conex.get_conection(), name_table)
                break
            else:
                print("\n¡ERROR!: Check The names of the columns and check the format necessary.")

    except TypeError as tyer:
        raise tyer

def execute_choise_8(conex: callable) -> None:
    """ execute the query select  """
    from mysql.connector import  Error
    
    COLUMN = ["id", "name", "email", "country", "age", "*"]

    while True:
        try:
            name_table: str = input("\nInserte the name table please ->: ").strip().lower()
            name_colums: str = input("Inserte the name of the columns ->: ").strip().lower()
            
            if re.search(r'\b[a-z]{2,}\b', name_table) and name_colums in COLUMN:
                select: object = Querys.SelectQuery()#object create from the module 'Querys' froom the class 'SelectQuery'
                select.execute_query(conex.get_conection(), name_colums, name_table)#call the method of the class 'SelectQuery'
                break
            else:
                print(f"\n¡ERROR! The column named '{name_colums}' does not exist")
        
        except Error as er:
            print(str(er) + ". Please check the fiel of the table name.")
            
def get_choise_admin(conex: callable, PROMPT: str) -> None:
    """ get the option of the user want execute """
    
    while True:
        
        try:
            number: str = int(input(PROMPT))
            if number == 1:
                execute_choise_1(conex)
                break
            if number == 8:
                execute_choise_8(conex)
                break
        except ValueError:
            print("\n¡ERROR! You need into a integer value. Please try again.")

def interface_user() -> None:
    """ Interface of the users """
    
    print("WLECOME TO THE DATABASE MANAGER".center(100))
    print("\nChoise the option (1) for create table.","\nChoise the option (8) for select data fron the table.")

def main():
    
    conex = Connection("localhost", "root", "Derrickrose1?", "users")
    
    try:
        interface_user()
        get_choise_admin(conex, "\nWhich option do you want to perform: ")
        
        
    except Exception as exp:
        print(f"\nAn error ocurred: {exp}\n")

if __name__=="__main__":
    main()
import sqlite3 as sql
import pickle as pck
import os
from t_logging import log_error

@log_error()
def load_data_dataset(PATH_FILE: str) -> list[tuple] | None:
    """ get the user's data fron the table with dataset"""
    
    if os.path.exists(PATH_FILE):
        
        with open(PATH_FILE, "rb") as rb:
            data = pck.load(rb)
            return data
    else:
        raise FileNotFoundError(f"\nERROR: FILENOTFOUND - The following path '{PATH_FILE}' not exist\n")

def dump_user_file(PATH_FILE: str, data_users: list[tuple]) -> None:
    """ we going to dump the user's data into the file 'data.bin' """
    
    if os.path.exists(PATH_FILE):
        if isinstance(data_users, list):
            
            with open(PATH_FILE, "wb") as wb:
                pck.dump(data_users, wb)
                print("\nThe data was saved successfully\n")
        else:
            raise ValueError("\nERROR: ValueError - The content of the variable 'data_users' is not a list\n")
    else:
        raise FileNotFoundError(f"\nERROR: FILENOTFOUND - The following path '{PATH_FILE}' not exist\n")

def add_users_table(PATH_DB: str, data_users: list[tuple]) -> None:
    """ insert  content to the table field."""

    try:
        if isinstance(data_users, list):
            
            conex = sql.connect(PATH_DB)
            cursor = conex.cursor()
            cursor.executemany("INSERT INTO users (id, nombre, age, country, email) VALUES (?,?,?,?,?)", data_users)
            
            if cursor.rowcount > 0:
                print("\nUser's data was saved successfully.\n")
                conex.commit()
            else:
                print("Upss, Something happened. Please check the query.")
                conex.rollback()
                
        else:
            raise ValueError("\nERROR: ValueError - The content of the variable 'data_users' is not a list\n")
        
    except sql.Error as er:
        print(er)
    finally:
        conex.close()
    
def main():
    
    PATH_DB = "sqlite3/user.db"
    PATH_FILE = "sqlit/data.bin"
    
    try:
        if isinstance(PATH_DB, str) and isinstance(PATH_FILE, str):
        
            data_users = load_data_dataset(PATH_FILE)
            
            #add_users_table(PATH_DB, data_users)
            
            
            #dump_user_file(PATH_FILE, data_users)
        
        else:
            raise Exception("\nPlease check the value of variable\n")
        
    except Exception as ex:
        print(ex)

if __name__=="__main__":
    main()
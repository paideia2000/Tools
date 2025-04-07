import sqlite3 as sql
import pandas as pd
import os
import matplotlib.pyplot as plt

def connection_db(path):
    """  """
    return sql.connect(path)

def select(path = None, 
        name_table = None, 
        filterrr = None
        ) -> None:
    """ """
    
    try:
        if path is  None and name_table is  None and filterrr is None:
            raise Exception("Please check the value of the variables, they cannot be None.")
        else:
            with sql.connect(path) as conex:
                
                query: str = f"Select {filterrr} FROM {name_table};"
                get_output = pd.read_sql_query(query, conex)
                get_output.plot(x="city", y="id", kind="bar" , figsize=(10,3), legend=False)
                
                plt.title("Testing")
                plt.xlabel("cities")
                plt.ylabel("user_id")
                plt.xticks(rotation = 90)
                plt.show()                
                # print(f"\nThe content to the table '{name_table}' is:", "\n")
                # print(get_output)
        
    except sql.OperationalError as fln:
        print("\n",fln)

def add_column(path = None, 
            name_table = None,  
            new_column = None) -> None:
    """  """
    try:
        if path is None and name_table is  None and new_column is None:
            raise Exception("Please check the value of the variables, they cannot be None.")
        else:
            with sql.connect(path) as conex:
                cursor = conex.cursor()
                #execute the query
                cursor.execute(f"ALTER TABLE {name_table} ADD {new_column} TEXT(50)")
                print("\nThe column was added successfully.\n")

    except sql.OperationalError as fln:
        raise fln

def rename_column_name(
    path = None,
    name_table = None, 
    old_column = None, 
    new_column = None
    ) -> None:
    """  """
    
    if not os.path.exists(path):
        raise FileNotFoundError("The path doens't exists.")
    
    try:
        if path is  None and name_table is  None and old_column is None and new_column is None:
            raise Exception("Please check the value of the variables, they cannot be None.")
        else:
            with sql.connect(path) as conex:
                cursor = conex.cursor()
                cursor.execute(f"ALTER TABLE {name_table} RENAME {old_column} TO {new_column};")
                print(f"\nThe name of the column {old_column} has been changed successfully to '{new_column}'\n")

    except sql.OperationalError as op:
        raise op
    except Exception as exp:
        raise exp

def drop_column(path = None, 
                name_table = None, 
                name_column = None
                ) -> None:
    """  """
    try:
        if path is None and name_table and name_column is None:
            raise Exception("Please check the value of the variables, they cannot be None.")
        else:
            with sql.connect(path) as conex:
                cursor = conex.cursor()
                
                cursor.execute(f"ALTER TABLE {name_table} DROP COLUMN {name_column};")
                print("\nThe column removed successfully\n")
        
    except sql.OperationalError as o:
        raise o
    
def main():
    
    PATH = "tools/sqlite3/test.db"
    
    try:
        if not os.path.exists(PATH):
            raise Exception("The database doesn't exists. Please make one.\n")

        
        #select(PATH, name_table="students", filterrr= "id, city")
        #add_column(PATH, name_table = "students", new_column = "email")
        #rename_column_name(PATH, name_table = "students", old_column = "void", new_column = "email")
        #drop_column(PATH, "students", "email")
        #
    
    except Exception as ex:
        print(f"\nAn error ocurred: {ex}\n")

if __name__=="__main__":
    main()
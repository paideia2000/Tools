import sys
import pandas as pd
from abc import ABC, abstractmethod
from mysql.connector import Error

class Interface(ABC):
    
    @abstractmethod
    def execute_query(self, conection, *args):
        pass

class CreateTableQuery(Interface):
    
    def execute_query(self, conection, name_table: str, *args):
        try:
            with conection as conex:
                cursor = conex.cursor()
                
                query = f""" CREATE TABLE IF NOT EXISTS {name_table} (
                    id INT NOT NULL AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    age INT NOT NULL,
                    country VARCHAR(50),
                    city VARCHAR(50) NOT NULL,
                    email VARCHAR(100) NOT NULL UNIQUE,
                    PRIMARY KEY (id)
                    ); """
                
                cursor.execute(query)
                conex.commit()
                print(f"\nThe table '{name_table}' created succesfully.")

        except Error as er:
            raise er

class SelectQuery(Interface):
    
    def execute_query(self, connection, filter_by: str, name_table: str) -> None:
        """ Execute the query SELECT """
    
        try:
            with connection as conex:
                cursor = conex.cursor()
                
                query = f"Select {filter_by} FROM {name_table}"
                cursor.execute(query)
                data = cursor.fetchall()
                
                df = pd.DataFrame(data)
                print("\n",df)
        
        except pd.errors.DatabaseError as pd_error:
            raise pd_error

class InsertQuery(Interface):
    
    def execute_query(cls, conection: callable, row_data: tuple):
        
        try:
            with conection as conex:
                cursor = conex.cursor()
                
                query = "INSERT INTO customers (name, age, country, email) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, row_data)
                conex.commit()
                
                print(f"\nThe data user added successfully to the database. Amount row(s) affected '{cursor.rowcount}'.")

        except Exception as e:
            raise  e# Re-lanza otras excepciones no esperadas

class UpdateQuery(Interface):
    
    def execute_query(self, conection, column_name: str,  data: tuple):
        
        try:
            
            with conection as conex:
                cursor = conex.cursor()
                
                query = "UPDATE customers SET {} = %s WHERE id = %s".format(column_name)

                cursor.execute(query, data)
                conex.commit()
                print(f"\nThe data was changed successfully. Amount row(s) affected '{cursor.rowcount}'.")
                
        except Error as er:
            raise er

class DeleteQuery(Interface):
    
    def execute_query(self, conection, name_table: str, user_id: int):
        
        try:
            with conection as conex:
                cursor = conex.cursor()
                
                query = "DELETE FROM {} WHERE id = %s".format(name_table)
                
                cursor.execute(query, (user_id,))
                conex.commit()
                print(f"\nThe data was deleted successfully. Amount row(s) affected '{cursor.rowcount}'.\n")
        except Error as er:
            raise type(er) from er

if __name__=="__main__":
    print("\nDont execute this script.")
    sys.exit()
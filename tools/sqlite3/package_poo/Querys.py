import pandas as pd
from abc import ABC, abstractmethod
from mysql.connector import Error

class Interface(ABC):
    
    @abstractmethod
    def execute_query(self, conection, *args):
        pass

class CreateTableQuery(Interface):
    
    def execute_query(self, conection, name_table: list, ):
        try:
            with conection as conex:
                cursor = conex.cursor()
                query = f""" CREATE TABLE IF NOT EXISTS {name_table} (
                    id INT NOT NULL AUTO_INCREMENT,
                    name VARCHAR(50) NOT NULL,
                    age INT NOT NULL,
                    COUNTRY VARCHAR(50),
                    email VARCHAR(100) NOT NULL,
                    PRIMARY KEY (id)
                    ) """
                cursor.execute(query)
                print("The table was created succesfully.")

        except Error as er:
            raise er

class SelectQuery(Interface):
    
    def execute_query(self, connection, filterr: str, name_table: str) -> None:
        """ Execute the query SELECT """
    
        try:
            with connection as conex:
                cursor = conex.cursor()
                
                query = f"Select {filterr} FROM {name_table}"
                cursor.execute(query)
                data = cursor.fetchall()
                
                df = pd.DataFrame(data)
                print(df)
        
        except Error as er:
            raise er
        except pd.errors.DatabaseError as pd_error:
            raise pd_error

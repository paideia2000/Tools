from mysql.connector import Error
from contextlib import contextmanager
import mysql.connector

class Connection():
    def __init__(self, localhost, user, password, database):
        self.__hostname = localhost
        self.__user = user
        self.__password = password
        self.__database = database
        
    @contextmanager
    def get_conection(self):
        """ Establishe Connection winth database """

        try:
            connex = mysql.connector.connect(
                host = self.__hostname,
                user = self.__user,
                password = self.__password,
                database = self.__database
                )
            
            print("\n✅ Connection established.\n") 
            
            yield connex
            
        except Error as e:
            raise e
        
        finally:
            if connex and connex.is_connected():
                print("\nThe connection is closed.\n")
                connex.close()

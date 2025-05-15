from mysql.connector import Error
import mysql.connector
from contextlib import contextmanager
import sys

class ConnectionPool:
    def __init__(self, hostname, username, password, database, pool_name = "poolconex", pool_size = 5):
        self.__hostame = hostname
        self.__username = username
        self.__password = password
        self.__database = database
        self.__pool_name = pool_name
        self.__pool_size = pool_size
        self.__pool = self.__createpool()
    
    def __createpool(self):
        """ create a pool connection """
        try:
            pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name = self.__pool_name,
                pool_size = self.__pool_size,
                host = self.__hostame,
                user = self.__username,
                password = self.__password,
                database = self.__database
            )
            return pool
            
        except Error as e:
            error_msg = f"Error creating connection pool: {e}"
            raise type(e)(error_msg) from e
    
    @contextmanager
    def connection(self):
        """ stablished the connection with the pool """
        
        connex = None
        try:
            
            connex = self.__pool.get_connection()
            
            yield connex

        except Error as e:
            error_msg = f"Error creating connection pool: {e}"
            raise type(e)(error_msg) from e
    
        
        finally:
            if connex and connex.is_connected():
                connex.close()

if __name__=="__main__":
    print("Don't execute this script")
    sys.exit()

import sys
from mysql.connector import Error
from contextlib import contextmanager
import mysql.connector

class ConnectionPool:
    def __init__(self, hostname, user, password, database, pool_name="mypool", pool_size=5):
        self.__hostname = hostname
        self.__user = user
        self.__password = password
        self.__database = database
        self.__pool_name = pool_name
        self.__pool_size = pool_size
        self.__pool = self.__create_pool()
        
    def __create_pool(self):
        """Create and return a connection pool"""
        try:
            pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name=self.__pool_name,
                pool_size=self.__pool_size,
                host=self.__hostname,
                user=self.__user,
                password=self.__password,
                database=self.__database
            )
            return pool
        
        except Error as e:
            print(f"Error creating connection pool: {e}")
            raise
            
    @contextmanager
    def connection(self):
        """Get a connection from the pool"""
        conn = None
        try:
            
            conn = self.__pool.get_connection()
            yield conn
        
        except Error as e:
            raise e
        finally:
            if conn and conn.is_connected():
                conn.close()  # Esto devuelve la conexión al pool


if __name__ == "__main__":
    print("\nDon't execute this script directly.")
    sys.exit()
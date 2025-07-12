import mysql.connector
from mysql.connector import Error
import pandas as pd
import matplotlib.pyplot as plt


def make_graphic():
    """  """

    try:
        
            connection = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="Derrickrose1?",
                database="graphic"
            )
            
            if connection.is_connected:
                query: str = "SELECT * FROM three";
                
                data = pd.read_sql_query(query, connection);
                
                
                plt.rcParams.update({
                        'font.size': 25,           # Tamaño base para textos (ejes, títulos, etc.)
                        'xtick.labelsize': 22,     # Tamaño de las etiquetas del eje X
                        'ytick.labelsize': 22,     # Tamaño de las etiquetas del eje Y
                    })
                
                data.plot(x="ejeX", y="ejeY", kind="bar", figsize=(10,5), legend=False)
                plt.title("Analisis del producto");
                plt.xticks(rotation=45)
                plt.show()

                
        
        
    except Error as er:
        raise type(er) from er
    finally:
        if connection.is_connected:
            connection.close()
    
    
    
    


def main():
    """  """
    
    try:
        
        make_graphic();
        
        
    except Exception as exp:
        print(f"An Error Ocurred: {exp}")
    
    
    
if __name__=="__main__":
    main()
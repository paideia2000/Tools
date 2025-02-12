""" 
Pedir al usuario:
-dominio
-ruta
-parametros de busqueda

Consturcción
-Eliminar espacios en blanco
-agregar https:// - sino hay
-debe haber "/" entre el dominio y la ruta
agregar "?" antes de los parametros
"""
from package.modu_test1 import obtener_dominio, obtener_ruta, obtener_parametros_buqueda,main
from random import shuffle

if __name__ == "__main__":
    main()
    

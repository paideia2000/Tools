from package.fun_read_write_txt import create_file, read_file, count_lines, count_words, poema_reverse

""" 
Crea un programa que lea un fichero de texto llamado "poema.txt". El programa debe:
Imprimir el contenido completo del fichero.
Contar el número de líneas del poema.
Contar el número de palabras en el poema.
Escribir el poema en un nuevo fichero llamado "poema_invertido.txt", 
pero con las líneas en orden inverso
"""

def catch_error_none(name_fichero: str, poema: str)-> str:
    """ Capturación de errores y campos vacios """
    try:
        
        if poema and name_fichero.endswith(".txt") and not all(espacios.isspace() for espacios in poema):
            create_file(name_fichero, poema)
            
            fichero_readding = read_file(name_fichero)
            print(f"\n{fichero_readding}\n")
            
            numbers_lines = count_lines(name_fichero)
            print(numbers_lines)
            
            numbers_words = count_words(name_fichero)
            print(numbers_words)
        else:
            print("\n¡ERROR! Compruebe el nombre del fichero -»(debe terminar con '.txt') o el contenido del poema que no este vacio.\n")
    
    except FileNotFoundError:
        print("¡ERROR! Compruebe la ruta del archivo.")

def main():
    """ ejecutar el programa """

    poema = "No perdono a la muerte enamorada,no perdono a la vida desatenta,no perdono a la tierra ni a la nada"
                
    catch_error_none("poema.txt",poema)#funsión que captura errores y sanetiza con condicionales
    
    print("\n","-"*63, "New_File_text_reverse", "-"*57,"\n")
    
    alreay_reverse = poema_reverse(poema)#variable que almacena el poema revertido
    
    create_file("poema_invertido.txt", alreay_reverse)

    read_new_file = read_file("poema_invertido.txt")
    print(read_new_file)
    
if __name__=="__main__":
    main()
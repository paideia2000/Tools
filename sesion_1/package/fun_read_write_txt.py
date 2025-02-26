def overwritten_file(path_file: str, content: str)-> str:
    """ creación de fichero """
    
    if content and not all(cont.isspace() for cont in content):
        
        with open(path_file, "w") as f:
            return f.write(content)
    
    else:
        print("\n¡ERROR! You should add contant to the file.\n")

def read_file(name_fichero: str)-> str:
    """ abrir el fichero en modo lectura """
    try:

        with open(name_fichero, "r") as r:
            return r.read()
        
    except FileNotFoundError:
        return "Error: el fichero no sea encontrado en la ruta."
        
def count_lines(name_fichero: str)-> int:
    """ contar el numero de lineas del fichero """
    try:
        
        with open(f"read_write_txt/{name_fichero}", "r") as conter_lines:
            amount_lines = conter_lines.readlines()
            return f"El fichero tiene -»{len(amount_lines)} lineas."
            
    except FileNotFoundError:
        return "Error: el fichero no sea encontrado en la ruta."
        
def count_words(name_ficher: str)-> int:
    """ contar el numero de letras del fichero """

    try:
        
        with open(f"contenido_json/{name_ficher}", "r", encoding="utf-8") as counter_words:
            number_words = list(espace for espace in counter_words.read() if espace != " ")
            return f"\nLa secuencia sin contar los espacios tiene -» {len(number_words)} letras."

    except FileNotFoundError:
        print("Error: el fichero no sea encontrado en la ruta.")

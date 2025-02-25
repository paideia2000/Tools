def create_file(name_fichero: str, contenido: str)-> str:
    """ creación de fichero """
    
    try:
        with open(f"read_write_txt/{name_fichero}", "w", encoding="utf-8") as make:
            return make.write(contenido)
    except TypeError:
        print("¡ERROR! Debe ingresar contenido válido para añadirlo al fichero.")
        
def read_file(name_fichero: str)-> str:
    """ abrir el fichero en modo lectura """
    try:

        with open(f"read_write_txt/{name_fichero}", "r") as r:
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
        with open(f"read_write_txt/{name_ficher}", "r", encoding="utf-8") as counter_words:
            number_words = list(espace for espace in counter_words.read() if espace is not " ")
            return f"\nLa secuencia sin contar los espacios tiene -» {len(number_words)} letras."

    except FileNotFoundError:
        print("Error: el fichero no sea encontrado en la ruta.")

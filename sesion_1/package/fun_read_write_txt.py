def create_file(name_fichero: str, contenido: str)-> str:
    """ creación de fichero """
    
    with open(f"read_write_txt/{name_fichero}", "w", encoding="utf-8") as make:
        return make.write(contenido)

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
            return f"El poema tiene -»{len(amount_lines)} lineas."
            
    except FileNotFoundError:
        return "Error: el fichero no sea encontrado en la ruta."
        
def count_words(name_ficher: str):
    """ contar el numero de letras del fichero """
    try:
        
        with open(f"read_write_txt/{name_ficher}", "r", encoding="utf-8") as counter_words:
            amount_words = counter_words.read()
            return f"\nEl numero de letras del poema es -»{len(amount_words)}"
    
    except FileNotFoundError:
        return "Error: el fichero no sea encontrado en la ruta."

#funsión que hace un reverse de una frase
def poema_reverse(poema: str)-> str:
    """ hacer un reverse al poema """
    
    if poema and not all(espace.isspace() for espace in poema):
        
        split_poema = poema.split()
        new_poema_reverse =  " ".join(split_poema[::-1])
        return new_poema_reverse.replace(",","\n")
    
    else:
        print("\nDebe insertar texto para poder revertirlo.\n")

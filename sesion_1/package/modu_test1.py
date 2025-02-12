def obtener_dominio(texto_para_input):#obteniendo el dominio de la url
    pedir_dominio = input(texto_para_input).strip().lower()
    
    if pedir_dominio:#verificar si "pedir_dominio" esta vacio
        if "https://" in pedir_dominio[:8]:
            return pedir_dominio
        else:#si en las primeras 8 letras del dominio no hay un "https://" se lo añadimos al str
            lista_dominio = pedir_dominio.split()
            dominio_correcto = ["https://"] + lista_dominio
            return "".join(dominio_correcto)
    
    else: 
        return "¡ERROR! Debe ingreasr un dominio válido."

def obtener_ruta(texto_para_input):#obteniendo la ruta de la url
    pedir_ruta = input(texto_para_input).strip().lower()
    
    if pedir_ruta:
        if "/" in pedir_ruta[:1]:
            return pedir_ruta
        else:
            ruta_correcta = ["/"] + pedir_ruta.split() + ["?"]
            return "".join(ruta_correcta)
    else:
        return "¡ERROR! Debe ingreasr un dominio válido."

def obtener_parametros_buqueda(texto_input):#obteniendo los parametros de busqueda de la url
    pedir_parametros_busqueda = input(texto_input).strip().lower()
    if pedir_parametros_busqueda:
        return pedir_parametros_busqueda
    else:
        return "¡ERROR! Debe ingreasr un dominio válido."

def main():
    
    dominio = obtener_dominio("Ingrese el Dominio por favor: ")
    ruta = obtener_ruta("Ingrese la ruta por favor: ")
    parametros_busqueda = obtener_parametros_buqueda("Ingrese los parametros de busqueda por favor: ")
    url = "".join([dominio,ruta,parametros_busqueda])
    
    print(f"El URL es el siguiente -» {url}")

def calculate_are_poligono(POLIGONO: dict) -> int | float:
    """ claculate the poligono area """
    
    
    if "triangulo" in POLIGONO.keys() :
        
        result_area_triangule = (POLIGONO["triangulo"]["base"] * POLIGONO["triangulo"]["altura"]) / 2
        
        return f"The area of the triangule is {result_area_triangule}"
    
    if "cuadrado" in POLIGONO.keys():
        
        result_area_cuadrado = POLIGONO["cuadrado"]["lado"] ** 2
        
        return f"The area of the cuadrado is {result_area_cuadrado}"
        
    if "rectangulo" in POLIGONO.keys():
        
        result_area_rectangulo = POLIGONO["rectangulo"]["base"] * POLIGONO["rectangulo"]["altura"]
        
        return f"The area of the cuadrado is {result_area_rectangulo}"



def main():
    
    POLIGONOS = [{"triangulo": {"base": 4, "altura": 6}}, {"cuadrado": {"lado": 2}}, {"rectangulo": {"base": 4, "altura": 6} }]
    
    for poligono in POLIGONOS:
    
        print(calculate_are_poligono(poligono))
        

main()
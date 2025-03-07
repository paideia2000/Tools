"""
Crea una clase llamada Tienda que tenga un atributo llamado inventario, 
que será un diccionario donde las claves son los nombres de los productos y los valores 
son sus cantidades en stock. Implementa un método para agregar productos al inventario y 
un método para eliminar productos.
Además, implementa el método mágico __len__ para devolver la cantidad de productos diferentes 
en el inventario.
Finalmente, crea un programa principal que agregue y elimine productos del inventario, 
y muestre cuántos productos diferentes hay en la tienda usando el método __len__.
"""
from test import Tienda

def make_instance() -> Tienda:
    """ Instantiating an object """
    
    tienda = Tienda()
    if isinstance(tienda, Tienda):
        return tienda
    else:
        raise TypeError

def get_product(prompt: str, instance: Tienda) -> None:
    """ get product to add to inventory """
    if prompt:
        
        contador = 3
        while contador > 0:
            product: str = input(prompt)
            
            if not product or not product.isalpha():
                contador -= 1
                print(f'¡ERROR! Please check the name of the product. You have "{contador}" attempts left.')
                
            else:
                instance.add_product(product)# (add_product) metodo de la clase tienda
                print(f'\nThe product "{product}" has been added successfully.\n')
                break
    else:
        raise ValueError

def remove_product(prompt: str, instance: Tienda) -> None:
    """ remevo a product of the inventory attribute"""
    if prompt:
        
        contador = 3
        while contador > 0:
            product: str = input(prompt).strip().upper()
            
            check_delete = instance.delete_product(product)# (delete_product) metodo de la clase tienda
            if check_delete is None:
                contador -= 1
                print(f"\nThe product doens't exist in the inventory. You have {contador} attempts left.")
            else:
                break
    else:
        raise ValueError

def show_products(instance: Tienda) -> dict:
    """ See inventory of the clase """
    
    print("\nPRODUCTS".ljust(20), "STOCK")
    print("-" * 38)
    for product, amount in instance.inventory.items():
        print(product.ljust(20), amount)

def user_interface(prompt: str)-> None:
    """  """
    print("\nInsert (1) to add product to inventory.","\n""Insert (2) to remove product to inventory.","\n""Insert (3) to see inevntory.")
    print("Insert (4) to exit the application.\n")
    
    instance: Tienda = make_instance()#instacia de la clase Tienda.

    while True:
        try:
            number_operation = int(input("Enter the number of the operation you wish to perform: "))
            if number_operation == 1:
                get_product(prompt, instance)
                break
            if number_operation == 2:
                remove_product(prompt, instance)
                break
            if number_operation == 3:
                show_products(instance)
                break
            if number_operation == 4:
                print("\nGood Bye\n")
                break
            if number_operation not in range(1,5):
                print("\n¡ERROR! You must choose a valid opcion. Try again please.\n")
            
        except ValueError :
            print("\n¡ERROR! Opción invalid. \n")

def main():
    
    try:
        
        user_interface("\nEnter the name of the product: ")
        
    except ValueError:
        print("\nPlease check the name of the product.")
    except TypeError:
        print("Error la instaciancia no puede ser none.")

if __name__=="__main__":
    main()

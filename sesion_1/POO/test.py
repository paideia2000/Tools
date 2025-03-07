class Tienda:
    def __init__(self,):
        self.__inventario = {"ASUS": 5, "RTX": 2 }

    @property
    def inventory(self):
        return self.__inventario

    def add_product(self, product: str):
        """ add product to store inventory """

        if product not in self.__inventario:
            self.__inventario[product] = 1

        else:
            self.__inventario[product] += 1

    def delete_product(self, product: str)-> bool:
        """ remove a product of the inventory """
        
        if product in self.__inventario:
            del self.__inventario[product]
            print(f'\nThe product "{product}" has been successfuly removed.\n')
            return True
        
        else:
            return None

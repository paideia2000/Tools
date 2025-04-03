import sys

class Phones:
    def __init__(self, punctuation: int, price: float, model="Smartphone", manufacturer="(No Indicado)", tipo="(No Indicado)"):
        self.tipo = tipo
        self.manufacturer = manufacturer
        self.model = model

        if isinstance(punctuation, (int,float)):
            self.__punctuation = punctuation
        else:
            raise AttributeError("\n¡ERROR! The value of the attribute '(PUNCTUATION and PRICE)' must be a number.\n")
        
        if isinstance(price, (int,float)) and price > 0:
            self.price = price
        else:
            raise AttributeError("\n¡ERROR! The value of the attribute '(PUNCTUATION and PRICE)' must be a number.\n")



    @property
    def get_punctuation(self):
        return self.__punctuation

    def __str__(self)-> str:
        return f'\nThe type is "{self.tipo}" manufactured by "{self.manufacturer}".\
        \nThe model {self.model} has a puntation of: "{self.__punctuation}", with a price of: "{self.price}".\n'



if __name__=="__main__":
    print("\nDon't do that!")
    sys.exit()


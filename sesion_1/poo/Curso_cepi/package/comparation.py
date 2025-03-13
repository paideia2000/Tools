from .phones import Phones

class Comparation(Phones):

    def __init__(self, punctuation: int, price: float, model="Smartphone", manufacturer="(No Indicado)", tipo="(No Indicado)"):
        super().__init__(punctuation, price, model, manufacturer, tipo)

    def qualityprice(self)-> int | float:
        """ get value for comparation """
        return ((self.get_punctuation ** 2 * 10)/ self.price)
    
    def __gt__(self, disp_2: Phones)-> bool:# Comparacion great than
        """ comaparation between phones who great than"""
        if self.tipo == disp_2.tipo:
            diference = self.qualityprice() - disp_2.qualityprice()
            return diference > 0# return true
        else:
            raise ValueError("\nThe phones aren't of the same type.")
    
    def __lt__(self, disp_2: Phones)-> bool:# menor que
        """ comaparation between phones who less than """
        
        if self.tipo == disp_2.tipo:
            diference = self.qualityprice() - disp_2.qualityprice()
            return diference < 0# return true
        else:
            raise ValueError("\nThe phones aren't of the same type.")


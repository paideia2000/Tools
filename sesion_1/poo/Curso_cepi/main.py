from package.comparation import Comparation
from deco_logging import log_anything

def check_who_is_better(disp_1: Comparation, disp_2: Comparation) -> str:
    """ return that phone is better using de magic method (gt-lt) """
    if disp_1 > disp_2:
        return f"\n The better phone is: {disp_1.manufacturer}, with their model: {disp_1.model}.\n"
    elif disp_1 < disp_2:
        return f"\n The better phone is: {disp_2.manufacturer}, with their model: {disp_2.model}.\n"
    else:
        return "\n The two phones have the same ralation price-quality"
        


@log_anything()
def check_who_is_better(disp_1: Comparation, disp_2: Comparation) -> str:
    """ return that phone is better using de magic method (gt-lt) """
    if isinstance(disp_1, Comparation) and isinstance(disp_2, Comparation):

        if disp_1 > disp_2:    
            return f"\nThe better phone is: {disp_1.manufacturer}, with their model: {disp_1.model}.\n"
        elif disp_1 < disp_2:
            return f"\nThe better phone is: {disp_2.manufacturer}, with their model: {disp_2.model}.\n"
        else:
            return "\nThe two phones have the same ralation price-quality"

@log_anything()
def order_by(list_phones: list, prompt: str) ->None:
    """ Order the phones by punctation or Price """
    while True:
        how = input(prompt).strip().lower()
        
        if not how:
            print("¡ERROR! That field cannot be empty")
        elif how == "s":
            list_phones.sort(key= lambda order_by: order_by.get_punctuation)
            print("\nPHONES ORDER BY PUNTUATION.")
            for phone in list_phones:
                print(f"\nPuntuation: {phone.get_punctuation}, Model: {phone.model}, Manufacturer by: {phone.manufacturer} Price: {phone.price}")
            break
        elif how == "p":
            list_phones.sort(key= lambda order_by: order_by.price)
            print("\nPHONES ORDER BY PRICE.")
            for phone in list_phones:
                print(f"\nPuntuation: {phone.get_punctuation}, Model: {phone.model}, Manufacturer by: {phone.manufacturer} Price: {phone.price}")
            break
        else:
            print(f"\n¡ERROR! Invalid option. You must enter the options (SCORE(S) or PRICE(P)).\n")

def main():
    PROMPT = "Sort the phone list by rating (S) or price (P): "

    try:
        p1 = Comparation(6,100, "Iphone 16", "Iphone")
        p2 = Comparation(5, 110, "Samsung s24", "Samsung")
        p3 = Comparation(8, 200, "Huawey tuf 15", "Huawey")
        p4 = Comparation(7, 220, "Xiamo Hierro 3", "Xiaomi")
        list_phones = [p1,p2,p3,p4]

        print(check_who_is_better(p1,p2))
        
        order_by(list_phones,PROMPT)

    except ValueError as vl:
        print(vl)
    except TypeError as ty:
        print(ty)
    
if __name__=="__main__":
    main()

@log_anything()
def main():
    PROMPT = "Sort the phone list by rating (S) or price (P): "

    p1 = Comparation(10, 100, "Iphone 16", "Iphone")
    p2 = Comparation(5, 110, "Samsung s24", "Samsung")
    p3 = Comparation(8, 200, "Huawey tuf 15", "Huawey")
    p4 = Comparation(7, 220, "Xiamo Hierro 3", "Xiaomi")
    list_phones = [p1,p2,p3,p4]

    print(check_who_is_better(p1,p2))
    
    order_by(list_phones,PROMPT)

if __name__=="__main__":
    try:
        main()
    
    except AttributeError as at:
        print(at)  
    except ValueError as vl:
        print(vl)

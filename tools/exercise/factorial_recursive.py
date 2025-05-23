
def factorial(number: int | float) -> int | float:
    """ calculate the factorial of the number, by recursividad"""

    if isinstance(number, int | float):

        if number == 1:
            return 1
        
        else:
            return number * factorial(number - 1)

    else:
        raise ValueError("ERROR: You must insert a numbers.") from ValueError

def main(number: int | float):

    
    try:
        
        print(factorial(number))
        
    except Exception as exp:
        print("\nAn Error Ocurred: {} \n".format(exp))
    
    


if __name__=="__main__":
    main(5)
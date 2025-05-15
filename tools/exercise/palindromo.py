def check_palindromo(phrase: str) -> bool:
    """ check if the expression is palindromo """
    import re
    
    if phrase and isinstance(phrase, str):
        wihtout_space = re.sub(r'[ .,:;]', "", phrase)
        
        if wihtout_space.lower() == wihtout_space.lower()[::-1]:
            
            return True
        
        else:
            return False
            
    else:
        raise ValueError("ERRROR: The content of the variable must be string ando cannot be empty.") 


def main():

    try:
        
        print(check_palindromo("Ana lleva al oso la avellana."))
        
    except Exception as exp:
        print("\n{}\n".format(exp))

if __name__=="__main__":
    main()
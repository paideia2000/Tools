def reverse_string(string: str) -> str:
    """ The function will going to return the reverse string """
    
    if string and isinstance(string, str):
        
        return string[::-1]

    else:
        raise ValueError("ERRROR: The string must be str ando cannot be empty")
    


try:
    print(reverse_string("Hola Mundo"))
except Exception as exp:
    print(f"\n {exp} \n")
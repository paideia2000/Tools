def check_expression(expression: str, sample: dict) -> bool:
    """  """

    
    if expression and isinstance(expression, str):
        
        pass
        
    else:
        raise ValueError("ERRROR: The string must be str ando cannot be empty") 


def main():
    
    sample = {")": "(", "}": "{", "]": "["}
    
    expression = "{ [ a * ( c + d ) ] - 5 }"
    
    try:
        
        check_expression(expression, sample)
        
    except Exception as exp:
        print("\n", exp, "\n")

if __name__=="__main__":
    main()
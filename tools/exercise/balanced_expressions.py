def check_expression(expression: str) -> bool:
    """  """
    import re
    
    miss_expresions = []
    
    if expression and isinstance(expression, str):
        
        new_expresion = re.findall(r'[()\[\]{}]', expression)
        
        for e in new_expresion:
            if e == "(":
                if ")" not in new_expresion:
                    miss_expresions.append(")")
                else:
                    continue
                    
            if e == "{":
                if "}" not in new_expresion:
                    miss_expresions.append("}")
                else:
                    continue
            
            if e == "[":
                if "]" not in new_expresion:
                    miss_expresions.append("]")
                else:
                    continue
        

        if not miss_expresions:
            return True
        else:
            
            return miss_expresions

    else:
        raise ValueError("ERRROR: The string must be str ando cannot be empty") 


def main():
    
    sample = {")": "(", "}": "{", "]": "["}
    
    expression = "{ [ a * ( c + d ) ] - 5 }"
    
    try:
        
        print(check_expression(expression))
        
    except Exception as exp:
        print("\n", exp, "\n")

if __name__=="__main__":
    main()
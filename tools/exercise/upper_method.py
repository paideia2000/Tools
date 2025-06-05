

    
def upper(alpha_characters: dict, PHRASE: str) -> str:
    """  Convert to upper the string """

    import re
    
    new_phrase: list = []
    
    
    if re.search(r"^[a-zA-Z]", PHRASE):
        
        for c in PHRASE:
            
            if c in alpha_characters.keys():
                
                new_phrase.append(alpha_characters[c])
                
            else:
                raise ValueError(f"\nThe character '{c}' isin't American Character.") 
        
    else:
        print("cannot")
    
    
    return "\n" + "".join(new_phrase) + "\n"

def main():
    
    
    PHRASE = "renecito el duro "
    
    indice_lower: list = [e for e in range(97, 123)]
    indice_upper: list = [e for e in range(65, 91)]
    alpha_characters = {chr(lower): chr(upper) for lower, upper in zip(indice_lower,indice_upper)}
    alpha_characters[" "] = " ";
    
    try:
        print(upper(alpha_characters, PHRASE))
    except Exception as ex:
        print("An Error Ocurred: {}".format(ex))
        

if __name__=="__main__":
    main()


    
def upper(DICT_UPPER: dict, PHRASE: str) -> str:
    """  Convert to upper the string """

    import re
    
    new_phrase: list = []
    
    
    if re.search(r"^[a-zA-Z]", PHRASE):
        
        for c in PHRASE:
            
            if c in DICT_UPPER.keys():
                
                new_phrase.append(DICT_UPPER[c])
                
            else:
                raise ValueError(f"\nThe character '{c}' isin't American Character.") 
        
    else:
        print("cannot")
    
    
    return "\n" + "".join(new_phrase) + "\n"

def main():
    
    
    PHRASE = "renecito el duro "
    
    DICT_UPPER = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G',
        'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N',
        'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U',
        'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z', ' ' : ' '
    }
    
    
    try:
        print(upper(DICT_UPPER, PHRASE))
    except Exception as ex:
        print("An Error Ocurred: {}".format(ex))
        

if __name__=="__main__":
    main()
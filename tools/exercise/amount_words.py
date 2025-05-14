def amount_words(phrase: str) -> dict:
    """ Count the number of words that are repeated """
    import re
    
    done = {}
    
    if phrase and isinstance(phrase, str):

        new_phrase = re.sub(r'[,.]', "", phrase).lower().split()
        
        for word in new_phrase:
            
            if word in done:
                done[word] += 1
            
            else:
                done[word] = 1
        
        return done
    
    else:
        
        raise ValueError("ERRROR: The string must be str ando cannot be empty")



phrase = "Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev)."

try:
    print(amount_words(phrase))
except Exception as exp:
    print(f"\n {exp} \n")
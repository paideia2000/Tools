def text_to_morse(phrase: str, morse_code_dict: dict) -> None:
    """ convert text to morse code """
    import re
    
    phrase_in_morse = []
    
    if phrase and isinstance(phrase, str):
        
        sanety_phrase = re.sub(r'[.,:;()]',"", phrase)
        
        for c in sanety_phrase.upper():
            
            if c in morse_code_dict.keys():
                phrase_in_morse.append(morse_code_dict[c])
            
        return " ".join(phrase_in_morse)

    else:
        raise ValueError("ERRROR: The string must be str ando cannot be empty") 
    


def main(phrase):
    
    
    morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..', ' ': '/',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }
    
    
    try:
        
        phrase_in_morse = text_to_morse(phrase, morse_code_dict)
        print(phrase_in_morse)
        
    except Exception as exp:
        print(f"\n {exp} \n")

if __name__=="__main__":
    main("Difruta del momento no pienses en el manyana")
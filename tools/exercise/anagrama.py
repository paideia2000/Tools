
def check_if_anagrama(word_1: str, word_2: str) -> str:
    """ check if the words are anagramas"""

    
    if word_1 and word_2:
        
        if all(letter.isalpha()  for letter in word_1) and all(letter.isalpha()  for letter in word_2):
            print(f"The word '{word_1}' if we make a sorted, we get the next word '{word_1[::-1]}'")
            print(f"The word '{word_2}' if we make a sorted, we get the next word '{word_2[::-1]}'")
        else:
            raise ValueError("ERROR: The word contain other character taht is not alphabetic.")
    
    else:
        raise ValueError("ERROR: Please check the content of the varibales")


def main():
    
    word_1 = "roma"
    word_2 = "hola"
    
    try:
        check_if_anagrama(word_1, word_2)
    except Exception as exp:
        print(exp)

if __name__=="__main__":
    main()

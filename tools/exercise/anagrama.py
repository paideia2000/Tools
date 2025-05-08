
def check_if_anagrama(word_1: str) -> None:
    """ check if the words are anagramas"""

    
    if word_1:
        
        
        if all(letter.isalpha()  for letter in word_1):
            return f"The word '{word_1}' if we make a sorted, we get the next word '{word_1[::-1]}'"

        else:
            raise ValueError("ERROR: The word contain other character taht is not alphabetic.")
    
    else:
        raise ValueError("ERROR: Please check the content of the varibales")


def main():
    
    
    word_1 = "roma"

    
    try:
        check_if_anagrama(word_1)
    except Exception as exp:
        print(exp)

if __name__=="__main__":
    main()

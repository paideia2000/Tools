def get_data(PROMPT_NAME: str, PROMPT_SEX: str) -> str:
    """  """
    import re
    
    while True:
        
        name: str = input(PROMPT_NAME).strip().lower()
        sex: str = input(PROMPT_SEX).strip().lower()
        
        
        if re.search(r'^[A-Za-z]+$', name) and sex == "male" or sex == "female":
            
            return name, sex
            
        else:
            print("\nERROR: The fiel only content alphabetic characters")


def give_pisition(name: str, sex: str) -> None:
    """  """
    
    if sex == "female" and ord(name[0]) <= ord("m") or sex == "male" and ord(name[0]) >= ord("m"):
        
        return "\nYou belong to group 'A'."
    
    else:
        
        return "\nYou belong to group 'B'."
    
    


def main(PROMPT_NAME, PROMPT_SEX):
    
    try:
        
        name, sex = get_data(PROMPT_NAME, PROMPT_SEX)
        
        print(give_pisition(name, sex))
        
    except Exception as ex:
        print("An Error Ocurred: ".format(ex))
        
        
if __name__=="__main__":
    main("\nEnter your name: ","\nEnter your sex: ")
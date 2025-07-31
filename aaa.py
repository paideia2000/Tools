
def get_number_PC()-> int:
    """     get the number choise pc """
    import random;
    
    number_List = random.choice(range(1,11));
    
    return number_List;
    

def get_number_player(PROMPT: str)-> int:
    """ get the player number choise """
    while(True):
        
        number = input(PROMPT)
        
        if(number.isdigit() and int(number) > 0 and int(number) < 11):
            
            return int(number)
        
        else:
            print(False)


def check_who_is_winner(number_PC: int, number_Player: int) -> None:
    """ check who is the winner """
    
    
    
    

def main():
    
    try:
        
        number_PC = get_number_PC();
        number_Player = get_number_player(PROMPT="Enter a number in the range (1-10)")
        
        check_who_is_winner(number_PC, number_Player)
        
    except Exception as exp:
        print("An error ocurred: {}".format(exp))



if __name__=="__main__":
    main()
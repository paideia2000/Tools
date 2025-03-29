from deco_logs import log_errors

@log_errors()
def get_choise_player(PROMPT: str, number_available: list[int]) -> int | None:
    """ the function must returned a integer number THAT IS THE POSITION ON THE BOARD of the player"""
    
    while True:
        try:
            position_user = int(input(PROMPT))
            if position_user >= 1 and position_user <= 9:
                if position_user not in number_available:
                    print("\n¡ERROR! That position is already selected.")
                else:
                    print(f"\nYou has taken the position '{position_user}'")
                    return position_user
            else:
                print(f"\n¡ERROR! Your choise '{position_user}' is out of range.")
        except ValueError:
            print(f"\n¡ERROR! Invalid Value, must be integer number.")
            raise

def get_choise_pc(number_available: list[int]) ->int | list[int]:
    """ get the moved of the pc """
    from random import choice
    move_pc = choice(number_available)
    print(f"\nThe PC has taken its position '{move_pc}'")
    return move_pc
    
def check_who_winner(moves_players: list[int], name=None) -> bool:
    """ check who playes is the winner """
    
    winner_combination = [
        (1,2,3),
        (4,5,6),
        (7,8,9),
        (1,4,7),
        (2,5,8),
        (3,6,9),
        (1,5,9),
        (3,5,7),
    ]
    
    for tupless in winner_combination:
        if all(pos in moves_players for pos in tupless):
            print(f"The winner is {name}")
            return True
    
    else:
        return False

def update_move(PROMPT: str):
    """ update the move in the board """
    pos = {i:i for i in range(1,10)}#position on the board 
    number_available = list(range(1,10))#numbers availables for obtein a position on the board
    choices_player = []
    choices_pc = []
    
    while True:
        if number_available:
            #PC turn on
            move_pc= get_choise_pc(number_available)
            number_available.remove(move_pc)
            choices_pc.append(move_pc)
            pos[move_pc] = "X"
            board(pos)
            get_bool_pc = check_who_winner(choices_pc, name="PC")
            if get_bool_pc:
                break
        if number_available:
            #Player turn on
            move_player = get_choise_player(PROMPT, number_available)
            number_available.remove(move_player)
            choices_player.append(move_player)
            pos[move_player] = "O"
            board(pos)
            get_bool_player = check_who_winner(choices_player, name="PLAYER")
            if get_bool_player:
                break
        else:
            print("\nThere is has been a tie.\n")
            break
        
def board(pos: dict) -> None:
    """ show the board """
    contador = 1
    for _ in range(0,3):
        print("+---------"*3 + "+")
        print("|".ljust(10)*4)
        for _ in range(0,3):
            print(f"|    {pos[contador]}".ljust(10), end="")
            contador += 1
        print("|")
        print("|".ljust(10)*4)
    print("+---------"*3+"+")

def interface() -> None:
    """ generate a user interface """
    print("WELCOME TO THE GAME (TIC-TAC-TOE).".center(130),"\nGAME REGULATIONS.")
    print("1 - The PC will be the first to play, with the \"X\" simbol.","\n2 - You will the second to play, with the \"O\" simbol.\n")

def main():
    
    try:
        interface()
        
        update_move("\nIs your turn. What position do you want play?: ")
    except Exception as exc:
        print(exc)
    
    
if __name__ == "__main__":
    main()
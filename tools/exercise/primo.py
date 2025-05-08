def if_primo(numb:int) -> bool:
    """ check if the number is primo """
    
    for n in range(2,numb):
        if numb % n == 0:
            return True
    else:
        return False
    
    

print(if_primo(17))
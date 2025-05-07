def print_fizz_buzz(LIMIT: int) -> None:
    """ Múltiplos de 3 por la palabra "fizz".
        Múltiplos de 5 por la palabra "buzz".
        Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz". """
        
    for n in range(LIMIT):
        if n % 3 == 0 and n % 5 == 0:
            print("FIZZBUZZ")
        elif n % 3 == 0:
            print("FIZZ")
        elif n % 5 == 0:
            print("BUZZ")
        else:
            print(n)
    


def main():
    
    LIMIT = 101
    print_fizz_buzz(LIMIT)


if __name__=="__main__":
    main()
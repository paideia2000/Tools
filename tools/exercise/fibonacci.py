def suce_fibonacci(limit: int) -> int|float:
    """ fibonacci sucesion """

    if isinstance(limit, int):
        
        if limit == 0:
            return 0
        elif limit == 1:
            return 1
        else:
            return suce_fibonacci(limit - 1) + suce_fibonacci(limit - 2)
    
    else:
        raise TypeError("Object cannot be interpreted as an integer")
    
    
def main():
    
    try:
        for limit in range(20):
            print(suce_fibonacci(limit))
            
    except Exception as exp:
        print("\n", exp, "\n")

if __name__=="__main__":
    main()
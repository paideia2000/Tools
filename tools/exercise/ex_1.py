

def sum_numb_list(lis_number: list[int]) -> int:
    """ sum all number of the list """
    
    from functools import reduce
    
    try:
        
        if isinstance(lis_number, list):
            if all(isinstance(num, int) for num in lis_number):
                
                result_sum: int = reduce(lambda x, y: x + y, lis_number)
                
                return result_sum
            
            else:
                raise TypeError("The value of the list must be integers.")

        else:
            raise ValueError(f"Please check the data type of the variable: '{type(lis_number)}'.")
    

    except Exception as exp:
        error_message = f"{exp}"
        raise type(exp)(error_message) from exp
    

def main():
    
    list_number: list = list(range(1,21))
    
    try:
        
        print(sum_numb_list(list_number))
        
    except Exception as exp:
        print(f"\nThe following error has ocurred: {exp}\n")

if __name__=="__main__":
    main()
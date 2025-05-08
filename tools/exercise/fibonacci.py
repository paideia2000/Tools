def suce_fibonacci(limit: int) -> int|float:
    """ fibonacci sucesion """

    if limit == 0:
        return 0
    elif limit == 1:
        return 1
    else:
        return suce_fibonacci(limit - 1) + suce_fibonacci(limit - 2)
    
    
for limit in range(20):
    print(suce_fibonacci(limit))
def fact(n : int):
    result = 1
    if not n:
        pass
    while n > 1:
        result *=n
        n-=1
    return result 

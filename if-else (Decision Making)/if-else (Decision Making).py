def compareNM(n : int, m : int):
    
    if n > m:
        return "greater"
    elif n == m :
        return "equal"
    else :
        return "lesser"

print (compareNM(4 , 5))
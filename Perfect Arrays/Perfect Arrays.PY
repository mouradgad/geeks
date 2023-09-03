def IsPerfect(arr):
#Complete the function
    if arr==arr[::-1]:
        return "perfect"
    else:
        return "not perfect"


arr = (1,2,3,2,1)
print (IsPerfect(arr))
                
        
    
def isDigitSumPalindrome(N):
    f = str(N)
    s=0
    for i in f:
        s+=int(i)
        
    d = str(s)

    j=d[::-1]
    if j == d:
        return 1
    else : 
        return 0

n= 1234

print (isDigitSumPalindrome(n))
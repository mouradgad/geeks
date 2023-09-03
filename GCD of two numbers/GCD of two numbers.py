import math

def gcd(A, B):
    if B == 0:
        return A
    else:
        return math.gcd(B, A % B)


print (gcd(3,4))
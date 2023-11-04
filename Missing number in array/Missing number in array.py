class Solution:
    def missingNumber(self,array,n):
        # code here
        f=0
        k=0
        for i in range (n+1):
            f+=i
        for j in array:
            k+=j
        z=f-k
        return z
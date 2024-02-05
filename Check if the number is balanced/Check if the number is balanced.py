class Solution:
    def balancedNumber(self, N):
        l=0
        r=0
        n=len(str(N))

        for i in range(len(str(N))):
            if i<n//2:
                l+=int(N[i])
                
            elif i>n//2:
                r+=int(N[i])

        if l==r:
            return 1
            
        return 0
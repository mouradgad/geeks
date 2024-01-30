import math
class Solution:
    def isPerfectNumber(self, N):
        # code here 
        if(N ==1):
            return 0
        sum = 0
        for i in range(1,int(math.sqrt(N)+1)):
            if(N%i==0):
                if(N/i!=N):
                    sum += i+(N/i)
                else: sum+=i
        if sum == N:
            return 1
        else:
            return 0
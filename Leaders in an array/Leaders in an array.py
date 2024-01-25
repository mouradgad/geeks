class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        max = A[N-1]
        result = [max]
        for i in range(N-2,-1,-1):
            if A[i] >= max:
                max = A[i]
                result.append(max)
        result.reverse()
        return result
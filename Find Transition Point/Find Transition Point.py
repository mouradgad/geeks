class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        for i in range(n):

            if arr[i]==1:

                return i

        return -1
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        if s > sum(arr):
            return [-1]
            
        i, j, total = 0, 0, 0
        
        while j < n:
            total += arr[j]
            while total > s and i<j:   
                total -= arr[i]
                i += 1
            if total == s:
                return [i+1, j+1]   
            j += 1
        return [-1]

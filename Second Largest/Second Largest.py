class Solution:

	def print2largest(self,arr, n):
		new_arr = sorted(set(arr))
        
        if len(new_arr) == 1:
            return -1
        else:    
            return new_arr[-2]
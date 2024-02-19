class Solution:
    def minJumps(self, arr, n):
        #code here
        idx = 0
        d = 0
        nn = n
        while True:
            val = arr[idx]
            if val == 0: return -1
            if (len(arr) == 1): break
            temp_val = arr[idx+1:val+idx+1]
            if (idx + val >= n-1):
                d+=1
                break
            val, i = max((v+i, i) for i, v in enumerate(temp_val))

            if idx + (val-i) >= n-1:
                d+=2
                break
            else:
                idx += (i+1)
                d+=1
            
        return d
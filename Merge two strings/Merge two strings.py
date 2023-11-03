class Solution:
    def merge(self, S1, S2):
        res=""
        i=0
        while i<len(S1) or i<len(S2):
            if i<len(S1):
                res += S1[i]
            
            if i<len(S2):
                res += S2[i]
            
            i=i+1
            
        return res

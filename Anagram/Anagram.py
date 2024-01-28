class Solution:
    
    def isAnagram(self,a,b):
        return sorted(a) == sorted(b)   
class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        a = list('abcdefghijklmnopqrstuvwxyz')
        s = s.lower()
        s = sorted(list(set(s)))
        if s[-26:] == a:
            return True
        else:
            return False
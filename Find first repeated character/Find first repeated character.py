class Solution:

    def firstRepChar(self, s):
        l = []
        for i in s:
            if i not in l:
                l.append(i)
            else:
                return i
                
        return -1
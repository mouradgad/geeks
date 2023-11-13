class Solution:
    def isSumPalindrome (self, n):
        # code here 
        if n == int(str(n)[::-1]):
            return n
        for i in range(5):
            n += int(str(n)[::-1])
            if n == int(str(n)[::-1]) :
                return n
        return -1
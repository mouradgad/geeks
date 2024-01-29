class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        n = len(str1)
        n1 = len(str2)
        if n != n1:
            return 0
        c = ''
        ac = ''
        ac = str2[n-2:n] + str2[0:n-2]
        c = str2[2:n] + str2[0:2]
        if c == str1 or ac == str1:
            return 1
        else:
            return 0
class Solution:
    def shortestDistance(s, word1, word2):
        # code here
        if word1==word2:
            return 0
        a=[]
        b=[]
        for i in range(len(s)):
            if s[i]==word1:
                a.append(i)
            elif s[i]==word2:
                b.append(i)
        res=len(s)
        for i in a:
            for j in b:
                res=min(res,abs(i-j))
        return res
    

S=["hi","hey","g","h"]
word1="hi"
word2="h"
print (Solution.shortestDistance(S,word1,word2))
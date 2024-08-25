class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = ""
        for i in s:
            if i.isalnum():  
                j += i.lower()  
        return j == j[::-1]  
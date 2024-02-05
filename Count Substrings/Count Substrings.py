class Solution:
	def countSubstr(self, S):
		# your code here
        count = S.count("1")
        return count*(count-1)//2
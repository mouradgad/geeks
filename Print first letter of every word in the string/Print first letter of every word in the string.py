class Solution:
	def firstAlphabet(self, S):
	    h=""
	    h+=S[0]
	    for i in range(len(S)):
	        if S[i] ==" ":
	            h+=S[i+1]
	    return (h)
class Solution:
    def getCompundInterest(self, P ,T , N , R):
        # code here
        a = P*((1+R/(N*100))**(N*T))
        return int(a)
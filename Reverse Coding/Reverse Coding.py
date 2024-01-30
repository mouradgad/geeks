class Solution:
    def sumOfNaturals(self, n):
        # code here 

        return int(((n*(n + 1))/2)%1000000007)
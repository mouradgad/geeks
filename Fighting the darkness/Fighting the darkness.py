class Solution:
    def maxDays(self, arr, n):
        # code here
        arr.sort()
        return arr[n-1]
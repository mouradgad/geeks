class Solution:
    def arraySortedOrNot(self, arr, n):
        if arr == sorted(arr):
            return 1
        else:
            return 0
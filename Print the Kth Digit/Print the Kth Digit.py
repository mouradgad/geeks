class Solution:
    def kthDigit(self, A, B, K):
        return int(str(A**B)[-K])
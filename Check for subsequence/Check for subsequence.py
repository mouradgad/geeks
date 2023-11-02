class Solution:
    def isSubSequence(self, A, B):
        j = 0
        for i in range(len(B)):
            if j < len(A):
                if B[i] == A[j]:
                    j += 1
        if j == len(A):
            return True
        else:
            return False
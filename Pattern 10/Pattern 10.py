class Solution:
    def printTriangle(self, N):
        for i in range(2*N-1):
            if i < N:
                print("* " * (i+ 1))
            else:
                print("* " * ((2*N) - i-1))
                
class Solution:
    def printTriangle(self, N):
        for i in range(N):
            print(" " * (N-i-1),end="")
            print("*" * (i+1),end="")
            print("*" * i) 
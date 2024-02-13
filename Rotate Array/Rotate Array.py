class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(A,D,N):
        #Your code here
        
        b=[]
        D = D % N
        for i in range(D,N):
            b.append(A[i])
        for i in range(0,D):
            b.append(A[i])
        for i in range(N):
            A[i]=b[i]
        return A


array = [1,2,3,4,5,6]
D=2
N=6

print (Solution.rotateArr(array,D,N))

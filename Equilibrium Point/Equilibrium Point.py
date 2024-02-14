# User function Template for python3
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        arr2=[]
        ans=0
        sum=0
        for i in A:
            sum=sum+i
            arr2.append(sum)
        total=arr2[len(arr2)-1]
        for j in range(1,len(A)):
            lsum=arr2[j]-A[j]
            rsum=total-arr2[j]
            if lsum==rsum:
                return j+1
                ans=ans+1
        if ans==0 and len(A)>1:
            return -1
        else:
            return 1
def nthTermOfAP(A1,A2,N):
    answer = A1+(N-1)*(A2-A1)
    return answer
        

w=2
r=3
N=4

print (nthTermOfAP(w,r,N))
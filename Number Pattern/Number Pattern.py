arr = []
N=6
for i in range(1,N+1):
    p=''
    for j in range(1,i+1):
        p+=str(j)
    for k in range (i-1,0,-1):
        p+=str(k)
    arr.append(int(p))
print(arr)
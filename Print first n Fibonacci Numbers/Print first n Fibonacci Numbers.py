res=[]
n1=0
n2=1
n=6
for i in range(n):
    if i==1:
        res.append(n2)
    else:
        n3=n1+n2
        res.append(n3)
        n1=n2
        n2=n3
    
print (res)
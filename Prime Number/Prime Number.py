N=4
count=0
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        count+=1
        if N/i!=i:
            count+=1
if count==2:
    print (1)
else:
    print (0)
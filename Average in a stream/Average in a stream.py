arr = (10,20,30,40,50)
l=[]
s=0
c=1
for i in arr:
    s+=i
    l.append(s/c)
    c+=1
print(l)

j=[]
a=(1,2,3,4,5)
b=(1,2,3)
for i in a:
    j.append(i)
for e in b:
    j.append(e)
r=list(set(j))
print(len(r))
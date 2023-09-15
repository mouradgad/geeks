a = (1,2,3)
b=(3,1,4)
cb = 0
ca= 0

for i in range (3):
    if a[i]>b[i]:
        ca+=1
    elif a[i]<b[i]:
        cb+=1
print (ca,cb)


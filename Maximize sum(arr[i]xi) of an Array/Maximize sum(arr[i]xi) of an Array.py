a=[1,2,3,4,5,6,7]
a.sort()
i=0
for j in range (len(a)):
    i+=j*a[j]
    
print (i%(10**9+7))
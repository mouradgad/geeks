dic={}
n=5
a=[1,2,3,3,4,5]
k=2
for i in range (n):
    if a[i] not in dic:
        dic[a[i]]=0
    dic[a[i]]+=1
    if dic[a[i]]==k:
        print (a[i])
    

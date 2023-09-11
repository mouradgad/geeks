n = 192
l=[]
digits=(str(n)+str(n*2)+str(n*3))
for j in digits:
        l.append(int(j))
        l.sort()
arr=[1,2,3,4,5,6,7,8,9]

if arr==l:
    print ("yes")
else : 
    print ("no")    


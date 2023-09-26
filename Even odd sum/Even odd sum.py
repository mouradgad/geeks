odd = 0
even = 0
Arr=(1,2,3,4,56,71,123)
for i in range(len(Arr)):
    if i%2 == 0:
        odd+=Arr[i]
    else :
        even +=Arr[i]
print (odd,even)

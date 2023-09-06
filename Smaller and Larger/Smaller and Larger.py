def getMoreAndLess(arr, x):
    # code here
    less = 0
    greater = 0
    for i in arr:
        if i >= x:
            greater +=1
        if i <=x:
            less +=1
    return less,greater

array = (1,2,3,5,6,7)

print (getMoreAndLess(array,2))


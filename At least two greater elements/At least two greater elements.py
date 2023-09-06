def findElements(a):
    # Your code goes here
    a.sort()
    s=2
    result = a[:-s]
    return result

array = [1,2,3,4,5,6,7]
print (findElements(array))
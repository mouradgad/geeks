arr=[1,2,3,4,5,6,7,8]
d=3
arr[:]=arr[d:]+arr[0:d]
print (arr)
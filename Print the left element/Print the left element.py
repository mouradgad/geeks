arr = (1, 23, 2, 41, 25, 1515, 1)
n = 7
arr = list(arr)  
arr.sort()
f = (n - 1) // 2

median = arr[f]
print(median)
matrix= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
a = 3 
b = 3
g = 0
for i in range(a):
    for j in range (b):
        g += matrix[i][j]
print (g)
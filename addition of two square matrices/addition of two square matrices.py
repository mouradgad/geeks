matrixA=[
    [1,2,3],
    [4,5,6]
]
matrixB=[
    [1,2,3],
    [4,5,6]
]
n = len(matrixA)

for i in range(n):
    for j in range(n):
        matrixA[i][j]+=matrixB[i][j]
print(matrixA)
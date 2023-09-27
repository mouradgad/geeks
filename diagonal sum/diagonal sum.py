sum = 0
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range(len(matrix)):
    sum += matrix[i][i] + matrix[i][len(matrix)-1-i]
print(sum)
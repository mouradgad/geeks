main = 0
Grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
secondary=0
b=len(Grid)
for i in range(b):
    main += Grid[i][i]
    secondary+= Grid[i][b-1-i]
difference = abs(main - secondary)
print(difference)
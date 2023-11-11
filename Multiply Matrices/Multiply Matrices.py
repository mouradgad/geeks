def multiply(A, B, C, n):

    for i in range(len(A)):

        for j in range(len(B)):

            for k in range(len(B[i])):
                C [i][j] += A[i][k] * B[k][j]
    return C
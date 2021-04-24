def rotate_matrix(matrix):
    N = len(matrix)
    for i in range(N):
        for j in range(i+1, N):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(N):
        for j in range(N//2):
            matrix[i][j], matrix[i][N-j-1] = matrix[i][N-j-1], matrix[i][j]

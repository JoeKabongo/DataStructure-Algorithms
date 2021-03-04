def zero_matrix_space(matrix):
    N = len(matrix)
    M = len(matrix[0])

    zero_rows = [False] * N
    zero_cols = [False] * M

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                zero_rows[i] = True
                zero_cols[j] = True

    for row in range(N):
        if zero_rows[row]:
            for col in range(M):
                matrix[row][col] = 0

    for col in range(M):
        if zero_cols[col]:
            for row in range(N):
                matrix[row][col] = 0


def zero_matrix_space(matrix):
    N = len(matrix)
    M = len(matrix[0])

    is_first_row_zero, is_first_col_zero = is_first_zero(matrix, N, M)

    for i in range(1, N):
        for j in range(1, M):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # make row zero
    for i in range(N):
        if matrix[i][0] == 0:
            make_row_zero(matrix, i, M)

    print(matrix)

    # make colum zero
    for i in range(M):
        if matrix[0][i] == 0:
            make_col_zero(matrix, i, N)

    if is_first_row_zero:
        make_row_zero(matrix, 0, M)

    if is_first_col_zero:
        make_col_zero(matrix, 0, N)


def make_row_zero(matrix, row, size):
    for i in range(size):
        matrix[row][i] = 0


def make_col_zero(matrix, col, size):
    for i in range(size):
        matrix[i][col] = 0


def is_first_zero(matrix, N, M):
    output = [False, False]
    for i in range(N):
        if matrix[i][0] == 0:
            output[1] = True
            break

    for j in range(M):
        if matrix[0][j] == 0:
            output[0] = True

    return output


x = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
zeroMatrixNoSpace(x)

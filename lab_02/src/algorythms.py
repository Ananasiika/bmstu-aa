import sys

def standart_alg(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    cols_b = len(mat_b[0])

    if cols_a != rows_b:
        return "Умножение невозможно. Число столбцов первой матрицы не равно числу строк второй матрицы."

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += mat_a[i][k] * mat_b[k][j]

    return result

def memory_standart_alg(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    cols_b = len(mat_b[0])

    if cols_a != rows_b:
        return "Умножение невозможно. Число столбцов первой матрицы не равно числу строк второй матрицы."

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += mat_a[i][k] * mat_b[k][j]

    size = 0

    size += sys.getsizeof(rows_a)
    size += sys.getsizeof(cols_a)
    size += sys.getsizeof(rows_b)
    size += sys.getsizeof(cols_b)

    size += sys.getsizeof(result)

    return size


def memory_vinograd_alg(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    cols_b = len(mat_b[0])

    size = 0

    size += sys.getsizeof(rows_a)
    size += sys.getsizeof(cols_a)
    size += sys.getsizeof(rows_b)
    size += sys.getsizeof(cols_b)

    result = [[0] * cols_b for _ in range(rows_a)]

    mul_row = [0] * rows_a
    mul_col = [0] * cols_b

    for i in range(rows_a):
        for j in range(cols_a // 2):
            mul_row[i] = mul_row[i] + mat_a[i][2 * j] * mat_a[i][2 * j + 1]

    for i in range(cols_b):
        for j in range(rows_b // 2):
            mul_col[i] = mul_col[i] + mat_b[2 * j][i] * mat_b[2 * j + 1][i]

    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = -mul_row[i] - mul_col[j]
            for k in range(cols_a // 2):
                result[i][j] = result[i][j] + (mat_a[i][2 * k] + mat_b[2 * k + 1][j]) * (mat_a[i][2 * k + 1] + mat_b[2 * k][j])

            if cols_a % 2 == 1:
                result[i][j] = result[i][j] + mat_a[i][cols_a - 1] * mat_b[rows_b - 1][j]

    size += sys.getsizeof(result)
    size += sys.getsizeof(mul_row)
    size += sys.getsizeof(mul_col)

    return size


def vinograd_alg(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    cols_b = len(mat_b[0])

    if cols_a != rows_b:
        return "Умножение невозможно. Число столбцов первой матрицы не равно числу строк второй матрицы."

    result = [[0] * cols_b for _ in range(rows_a)]

    mul_row = [0] * rows_a
    mul_col = [0] * cols_b

    for i in range(rows_a):
        for j in range(cols_a // 2):
            mul_row[i] = mul_row[i] + mat_a[i][2 * j] * mat_a[i][2 * j + 1]

    for i in range(cols_b):
        for j in range(rows_b // 2):
            mul_col[i] = mul_col[i] + mat_b[2 * j][i] * mat_b[2 * j + 1][i]

    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = -mul_row[i] - mul_col[j]
            for k in range(cols_a // 2):
                result[i][j] = result[i][j] + (mat_a[i][2 * k] + mat_b[2 * k + 1][j]) * (mat_a[i][2 * k + 1] + mat_b[2 * k][j])

            if cols_a % 2 == 1:
                result[i][j] = result[i][j] + mat_a[i][cols_a - 1] * mat_b[rows_b - 1][j]

    return result

def memory_optimized_vinograd_alg(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    cols_b = len(mat_b[0])

    size = 0

    size += sys.getsizeof(rows_a)
    size += sys.getsizeof(cols_a)
    size += sys.getsizeof(rows_b)
    size += sys.getsizeof(cols_b)

    if cols_a != rows_b:
        return "Умножение невозможно. Число столбцов первой матрицы не равно числу строк второй матрицы."

    result = [[0] * cols_b for _ in range(rows_a)]

    mul_row = [0] * rows_a
    mul_col = [0] * cols_b

    for i in range(rows_a):
        for j in range(cols_a >> 1):
            mul_row[i] += mat_a[i][j << 1] * mat_a[i][(j << 1) + 1]

    for i in range(cols_b):
        for j in range(rows_b >> 1):
            mul_col[i] += mat_b[j << 1][i] * mat_b[(j << 1) + 1][i]

    flag = cols_a % 2

    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = -mul_row[i] - mul_col[j]

            for k in range(1, cols_a, 2):
                result[i][j] += (mat_a[i][k - 1] + mat_b[k][j]) * (mat_a[i][k] + mat_b[k - 1][j])

            if flag:
                result[i][j] += mat_a[i][cols_a - 1] * mat_b[rows_b - 1][j]

    size += sys.getsizeof(result)
    size += sys.getsizeof(flag)
    size += sys.getsizeof(mul_col)
    size += sys.getsizeof(mul_row)

    return size

def optimized_vinograd_alg(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    cols_b = len(mat_b[0])

    if cols_a != rows_b:
        return "Умножение невозможно. Число столбцов первой матрицы не равно числу строк второй матрицы."

    result = [[0] * cols_b for _ in range(rows_a)]

    mul_row = [0] * rows_a
    mul_col = [0] * cols_b

    for i in range(rows_a):
        for j in range(cols_a >> 1):
            mul_row[i] += mat_a[i][j << 1] * mat_a[i][(j << 1) + 1]

    for i in range(cols_b):
        for j in range(rows_b >> 1):
            mul_col[i] += mat_b[j << 1][i] * mat_b[(j << 1) + 1][i]

    flag = cols_a % 2

    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = -mul_row[i] - mul_col[j]

            for k in range(1, cols_a, 2):
                result[i][j] += (mat_a[i][k - 1] + mat_b[k][j]) * (mat_a[i][k] + mat_b[k - 1][j])

            if flag:
                result[i][j] += mat_a[i][cols_a - 1] * mat_b[rows_b - 1][j]

    return result


def strassen_alg(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    cols_b = len(mat_b[0])

    if cols_a != rows_b:
        return "Умножение невозможно. Число столбцов первой матрицы не равно числу строк второй матрицы."

    size = max(rows_a, cols_a, rows_b, cols_b)
    size = 2 ** (size - 1).bit_length()

    A_padded = [[0] * size for _ in range(size)]
    B_padded = [[0] * size for _ in range(size)]

    for i in range(rows_a):
        for j in range(cols_a):
            A_padded[i][j] = mat_a[i][j]

    for i in range(rows_b):
        for j in range(cols_b):
            B_padded[i][j] = mat_b[i][j]

    C_padded = strassen_recursive(A_padded, B_padded)

    C = []
    for i in range(rows_a):
        C.append(C_padded[i][:cols_b])

    return C

def strassen_recursive(mat_a, mat_b):
    n = len(mat_a)

    if n == 1:
        return [[mat_a[0][0] * mat_b[0][0]]]
    
    mid = n // 2
    A11 = [mat_a[i][:mid] for i in range(mid)]
    A12 = [mat_a[i][mid:] for i in range(mid)]
    A21 = [mat_a[i][:mid] for i in range(mid, n)]
    A22 = [mat_a[i][mid:] for i in range(mid, n)]
    B11 = [mat_b[i][:mid] for i in range(mid)]
    B12 = [mat_b[i][mid:] for i in range(mid)]
    B21 = [mat_b[i][:mid] for i in range(mid, n)]
    B22 = [mat_b[i][mid:] for i in range(mid, n)]
    
    
    M1 = strassen_recursive(matrix_add(A11, A22), matrix_add(B11, B22))
    M2 = strassen_recursive(matrix_add(A21, A22), B11)
    M3 = strassen_recursive(A11, matrix_sub(B12, B22))
    M4 = strassen_recursive(A22, matrix_sub(B21, B11))
    M5 = strassen_recursive(matrix_add(A11, A12), B22)
    M6 = strassen_recursive(matrix_sub(A11, A21), matrix_add(B11, B12))
    M7 = strassen_recursive(matrix_sub(A12, A22), matrix_add(B21, B22))
    
    
    C11 = matrix_add(matrix_sub(matrix_add(M1, M4), M5), M7)
    C12 = matrix_add(M3, M5)
    C21 = matrix_add(M2, M4)
    C22 = matrix_sub(matrix_sub(matrix_add(M1, M3), M2), M6)
    
    
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid, n):
        C.append(C21[i-mid] + C22[i-mid])
    
    return C
    

def matrix_add(mat_a, mat_b):
    return [[mat_a[i][j] + mat_b[i][j] for j in range(len(mat_a[i]))] for i in range(len(mat_a))]

def matrix_sub(mat_a, mat_b):
    return [[mat_a[i][j] - mat_b[i][j] for j in range(len(mat_a[i]))] for i in range(len(mat_a))]



def memory_strassen_alg(mat_a, mat_b):
    rows_a = len(mat_a)
    cols_a = len(mat_a[0])
    rows_b = len(mat_b)
    cols_b = len(mat_b[0])

    memory = 0

    memory += sys.getsizeof(rows_a)
    memory += sys.getsizeof(cols_a)
    memory += sys.getsizeof(rows_b)
    memory += sys.getsizeof(cols_b)

    if cols_a != rows_b:
        return "Умножение невозможно. Число столбцов первой матрицы не равно числу строк второй матрицы."

    size = max(rows_a, cols_a, rows_b, cols_b)
    size = 2 ** (size - 1).bit_length()

    A_padded = [[0] * size for _ in range(size)]
    B_padded = [[0] * size for _ in range(size)]

    for i in range(rows_a):
        for j in range(cols_a):
            A_padded[i][j] = mat_a[i][j]

    for i in range(rows_b):
        for j in range(cols_b):
            B_padded[i][j] = mat_b[i][j]


    memory += sys.getsizeof(size)
    memory += sys.getsizeof(A_padded)
    memory += sys.getsizeof(B_padded)

    memory += memory_strassen_recursive(A_padded, B_padded)

    return memory

def memory_strassen_recursive(mat_a, mat_b):
    n = len(mat_a)

    memory = 0
    memory += sys.getsizeof(len)

    if n == 1:
        return memory + sys.getsizeof([[mat_a[0][0] * mat_b[0][0]]])
    
    mid = n // 2
    A11 = [mat_a[i][:mid] for i in range(mid)]
    A12 = [mat_a[i][mid:] for i in range(mid)]
    A21 = [mat_a[i][:mid] for i in range(mid, n)]
    A22 = [mat_a[i][mid:] for i in range(mid, n)]
    B11 = [mat_b[i][:mid] for i in range(mid)]
    B12 = [mat_b[i][mid:] for i in range(mid)]
    B21 = [mat_b[i][:mid] for i in range(mid, n)]
    B22 = [mat_b[i][mid:] for i in range(mid, n)]

    memory += sys.getsizeof(mid)
    memory += sys.getsizeof(A11)
    memory += sys.getsizeof(A12)
    memory += sys.getsizeof(A21)
    memory += sys.getsizeof(A22)
    memory += sys.getsizeof(B11)
    memory += sys.getsizeof(B12)
    memory += sys.getsizeof(B21)
    memory += sys.getsizeof(B22)

    memory += memory_strassen_recursive(matrix_add(A11, A22), matrix_add(B11, B22))
    # memory += memory_strassen_recursive(matrix_add(A21, A22), B11)
    # memory += memory_strassen_recursive(A11, matrix_sub(B12, B22))
    # memory += memory_strassen_recursive(A22, matrix_sub(B21, B11))
    # memory += memory_strassen_recursive(matrix_add(A11, A12), B22)
    # memory += memory_strassen_recursive(matrix_sub(A11, A21), matrix_add(B11, B12))
    # memory += memory_strassen_recursive(matrix_sub(A12, A22), matrix_add(B21, B22))

    M1 = strassen_recursive(matrix_add(A11, A22), matrix_add(B11, B22))
    M2 = strassen_recursive(matrix_add(A21, A22), B11)
    M3 = strassen_recursive(A11, matrix_sub(B12, B22))
    M4 = strassen_recursive(A22, matrix_sub(B21, B11))
    M5 = strassen_recursive(matrix_add(A11, A12), B22)
    M6 = strassen_recursive(matrix_sub(A11, A21), matrix_add(B11, B12))
    M7 = strassen_recursive(matrix_sub(A12, A22), matrix_add(B21, B22))

    
    C11 = matrix_add(matrix_sub(matrix_add(M1, M4), M5), M7)
    C12 = matrix_add(M3, M5)
    C21 = matrix_add(M2, M4)
    C22 = matrix_sub(matrix_sub(matrix_add(M1, M3), M2), M6)

    memory += sys.getsizeof(C11)
    memory += sys.getsizeof(C12)
    memory += sys.getsizeof(C21)
    memory += sys.getsizeof(C22)
    
    
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid, n):
        C.append(C21[i-mid] + C22[i-mid])
    
    memory += sys.getsizeof(C)

    return memory
    
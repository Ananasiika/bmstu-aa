def damerau_levenshtein_matrix(str1, str2, output = True):
    m = len(str1)
    n = len(str2)
    
    matrix = create_matrix(m + 1, n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,         
                               matrix[i][j - 1] + 1,        
                               matrix[i - 1][j - 1] + cost) 

            if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j - 1]:
                matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + 1)

    if output:
        print("\nМатрица для расстояния Дамерау-Левенштейна:")
        print_matrix(matrix, str1, str2)

    return matrix[m][n]


def create_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]

    for i in range(n):
        matrix[i][0] = i
    
    for j in range(m):
        matrix[0][j] = j

    return matrix
    

def print_matrix(matrix, str1, str2):
    print("\n0  0  " + "  ".join([let for let in str2]))

    for i in range(len(str1) + 1):
        
        print(str1[i - 1] if (i != 0) else "0", end = "")

        for j in range(len(str2) + 1):

            print("  " + str(matrix[i][j]), end = "")

        print()


def levenshtein_matrix(str1, str2, output = True):
    m = len(str1)
    n = len(str2)

    matrix = create_matrix(m + 1, n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1

            matrix[i][j] = min(matrix[i - 1][j] + 1,         
                               matrix[i][j - 1] + 1,         
                               matrix[i - 1][j - 1] + cost)  

    if (output):
        print("\nМатрица для расстояния Левенштейна:")
        print_matrix(matrix, str1, str2)

    return matrix[m][n]

def damerau_levenshtein_cache_recursive(str1, str2, output = True):
    cache = {}

    def damerau_levenshtein_recursive(str1, str2):
        if (str1, str2) in cache:
            return cache[(str1, str2)]

        if len(str1) == 0:
            return len(str2)
        if len(str2) == 0:
            return len(str1)
        
        deletion = damerau_levenshtein_recursive(str1[:-1], str2) + 1
        insertion = damerau_levenshtein_recursive(str1, str2[:-1]) + 1
        substitution = damerau_levenshtein_recursive(str1[:-1], str2[:-1]) + (str1[-1] != str2[-1])
        transposition = float('inf')

        if len(str1) > 1 and len(str2) > 1 and str1[-1] == str2[-2] and str1[-2] == str2[-1]:
            transposition = damerau_levenshtein_recursive(str1[:-2], str2[:-2]) + 1

        result = min(deletion, insertion, substitution, transposition)
        cache[(str1, str2)] = result
        return result

    distance = damerau_levenshtein_recursive(str1, str2)

    return distance


def damerau_levenshtein_recursive(str1, str2, output = True):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    flag = 0 if (str1[-1] == str2[-1]) else 1

    add = damerau_levenshtein_recursive(str1[:-1], str2) + 1
    delete = damerau_levenshtein_recursive(str1, str2[:-1]) + 1
    change = damerau_levenshtein_recursive(str1[:-1], str2[:-1]) + flag
    transposition = damerau_levenshtein_recursive(str1[:-2], str2[:-2]) + 1

    if (len(str1) > 1 and len(str2) > 1 and str1[-1] == str2[-2] and str1[-2] == str2[-1]):
        minimum  = min(add, delete, change, transposition)
    else:
        minimum = min(add, delete, change)

    return minimum
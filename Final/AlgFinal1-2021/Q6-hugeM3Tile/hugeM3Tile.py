MOD = 44711

def mat_mult(A, B):
    size = len(A)
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result

def mat_pow(matrix, power):
    size = len(matrix)
    result = [[1 if i == j else 0 for i in range(size)] for j in range(size)]  # Identity matrix
    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, matrix)
        matrix = mat_mult(matrix, matrix)
        power //= 2
    return result

def f(L):
    if L % 2 != 0:  # If L is odd, return 0
        return 0
    elif L == 0:
        return 1
    elif L == 2:
        return 3

    # Transformation matrix
    M = [[4, -1], [1, 0]]

    # Initial vector [f(2), f(0)]
    F_init = [3, 1]

    # Exponent for transformation matrix is (L//2 - 1)
    M_exp = mat_pow(M, L // 2 - 1)

    # Multiplying the matrix with the initial vector
    F_L = [sum(M_exp[i][j] * F_init[j] for j in range(2)) % MOD for i in range(2)]
    return F_L[0]

# Test cases
print(f(4999998))        # Expected output: 28306
print(f(4999999998))     # Expected output: 36159

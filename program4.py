import numpy as np

def split(A, mid):
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    return A11, A12, A21, A22


def combine(C11, C12, C21, C22):
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))

    return np.vstack((top, bottom))


def strassen(A, B):
    n = A.shape[0]

    if n == 1:
        return A * B

    mid = n // 2

    A11, A12, A21, A22 = split(A, mid)
    B11, B12, B21, B22 = split(B, mid)

    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 + M3 - M2 + M6

    return combine(C11, C12, C21, C22)


def next_power_of_2(n):
    size = 1

    while size < n:
        size *= 2

    return size


def pad_matrix(A, size):
    n = A.shape[0]

    padded = np.zeros((size, size), dtype=A.dtype)
    padded[:n, :n] = A

    return padded


def strassen_multiply(A, B):
    n = A.shape[0]

    size = next_power_of_2(n)

    A_padded = pad_matrix(A, size)
    B_padded = pad_matrix(B, size)

    C_padded = strassen(A_padded, B_padded)

    C = C_padded[:n, :n]

    return C


A = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

B = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

C = strassen_multiply(A, B)

print("Result:")
print(C)

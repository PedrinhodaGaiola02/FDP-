import numpy as np

def jacobi(A, b, x0, tolerance):
    x = x0
    iterations = 0

    while True:
        iterations += 1
        D = np.diag(A) * np.identity(len(A))
        R = A - D
        next_x = (b - R@x) / np.diag(A)

        if abs(np.linalg.norm(next_x - x) < tolerance):
            break

        x = next_x

    return x, iterations

A = [
    [3, -1, -1],
    [-1, 3, -1],
    [-1, -1, 3]
]

b = [1, 2, 3]

resultado, iteracoes = jacobi(A, b, [0, 0, 0], 10**(-10))

print(resultado)

import numpy as np

def potencias(A, x0, iterations):
    x = x0

    for i in range(iterations):
        y = A @ x
        x = y / np.linalg.norm(y)

        Y = np.transpose(x) @ A @ x

    return x, Y


A = np.array([
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3],
])

A2 = np.diag(np.random.rand(3))

x0 = np.array([1, 1, 1])

print(potencias(A, x0, 10))
print(potencias(A2, x0, 10))

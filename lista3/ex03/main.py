import numpy as np
from matplotlib import pyplot as plt

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
    [3, -1],
    [-2, 4]
]

b = [2, 1]
x0 = [0, 0]

erros = [
    ("10^(-2)",  10**(-2) ),
    ("10^(-3)",  10**(-3) ),
    ("10^(-4)",  10**(-4) ),
    ("10^(-5)",  10**(-5) ),
    ("10^(-6)",  10**(-6) ),
    ("10^(-7)",  10**(-7) ),
    ("10^(-8)",  10**(-8) ),
    ("10^(-9)",  10**(-9) ),
    ("10^(-10)", 10**(-10)),
    ("10^(-11)", 10**(-11)),
    ("10^(-12)", 10**(-12)),
]

eixo_x = np.zeros(len(erros))
eixo_y = np.zeros(len(erros))

for (label, erro) in erros:
    x, iterations = jacobi(A, b, x0, erro)
    print("{}: {}".format(label, x))

    eixo_y[erros.index((label, erro))] = iterations
    eixo_x[erros.index((label, erro))] = np.log10(erro)

print(eixo_x)
print(eixo_y)

plt.plot(eixo_x, eixo_y)
plt.xlabel('log10(erro)')
plt.ylabel('iteracoes')
plt.xticks([
    np.log10(10**(-2)),
    np.log10(10**(-3)),
    np.log10(10**(-4)),
    np.log10(10**(-5)),
    np.log10(10**(-6)),
    np.log10(10**(-7)),
    np.log10(10**(-8)),
    np.log10(10**(-9)),
    np.log10(10**(-10)),
    np.log10(10**(-11)),
    np.log10(10**(-12)),
])
plt.show()

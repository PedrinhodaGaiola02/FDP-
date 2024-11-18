import numpy as np
from functions import f, df


def newton(f, df, x0, tolerance):
    x = x0
    iterations = 0

    while True:
        iterations += 1
        x = x - f(x) / df(x)

        if abs(f(x)) < tolerance:
            break

    return x, iterations

x, iterations = newton(f, df, 0, 0.00000000000000000000000000000000000000000000001)
print("Raiz: {}, Iteracoes: {}".format(x, iterations))

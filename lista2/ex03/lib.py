import math

def calcula_pi(A):
    dx = 1 / A
    soma_de_riemann = 0
    F = []

    for i in range(1, A + 1):
        x = i * dx
        F_i = math.sqrt(1 - x ** 2) if x ** 2 <= 1 else 0
        soma_de_riemann += F_i * dx

    π = 4 * soma_de_riemann
    erro = abs(math.pi - π)
    return dx, x, F, soma_de_riemann, π, erro



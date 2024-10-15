import math

def calcula_pi(A):
    Δx = 1 / A
    Soma_de_Riemann = 0
    F = []

    for i in range(1, A + 1):
        x = i * Δx
        F_i = math.sqrt(1 - x ** 2) if x ** 2 <= 1 else 0  
        Soma_de_Riemann += F_i * Δx

    π = 4 * Soma_de_Riemann
    erro = abs(math.pi - π)  
    return Δx, x, F, Soma_de_Riemann, π, erro



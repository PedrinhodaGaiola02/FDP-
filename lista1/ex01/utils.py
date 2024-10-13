def combinacao_linear(a, A, b, B):
    resultado = a * A + b * B
    return resultado

def potencia(matriz, exp):
    resultado = matriz
    
    for i in range(exp - 1):
        resultado = resultado @ matriz
    
    return resultado

#Função usada para somar os valores dos dados 

def soma(A, B):
    B = []
    soma = 0
    for i in range(A):
        for j in B:
            soma = soma + j
    return soma

#Jogar um dado podendo cair um número aleatório entre 1 e 6
import random 
from somatorio import soma as soma_valor_dados 

M = 1
N = 1
D = []

for i in range(M):
    for j in range(N):
        D.append(random.uniform(0, 6))
        print(D)

Soma = soma_valor_dados(M, D)
print(D)
print(Soma)





#Jogar M dados




#Jogar esses M dados N vezes


#Somar cada um dos valores dos dados


#Criar o histograma
#Jogar um dado podendo cair um número aleatório entre 1 e 6
import random 
from Soma import soma 

M = 1
N = 1
D = []

for i in range(M):
    for j in range(N):
        D.append(random.randint(0, 6))
        

Soma = soma(M, D)
print(D)
print(Soma)





#Jogar M dados




#Jogar esses M dados N vezes


#Somar cada um dos valores dos dados


#Criar o histograma
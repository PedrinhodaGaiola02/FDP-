import matplotlib.pyplot as plt
import numpy as np

def phi(x):
    phi = 1/np.sqrt(x)
    return phi 

x_velho = 0.75

iteracoes = 2
valores_de_x = [x_velho]
valores_da_funcao = []

for i in range(iteracoes):
    x_novo = phi(x_velho)
    valores_da_funcao.append(phi(x_velho))
    valores_de_x.append(x_novo)
    x_velho = x_novo
    print('Valor de X:', valores_de_x)
    print('Valor de da funcao:', valores_da_funcao)

def y(x):
    return x

eixo_x = np.linspace(0, 1.5)

plt.figure(figsize=(8, 6))
plt.plot(eixo_x, phi(eixo_x), label='phi(x)')
plt.plot(eixo_x, y(eixo_x), linestyle='--', label='y = x')


for i in range(iteracoes):
    plt.scatter(valores_de_x[i], valores_da_funcao[i], color='red')  # Pontos (x, phi(x))
    plt.scatter(valores_de_x[-1], valores_de_x[-1], color='red')
    plt.plot([valores_de_x[i], valores_de_x[i]], [valores_de_x[i], valores_da_funcao[i]], color='red')  # Linha vertical contínua
    plt.plot([valores_de_x[i], valores_da_funcao[i]], [valores_da_funcao[i], valores_da_funcao[i]], color='red')  # Linha horizontal contínua
    

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Iterações da Função phi(x)')
plt.grid(True)
plt.show()    
##Exercício 2
import numpy as np
import time 
import matplotlib.pyplot as plt

dimenm = [10, 15, 20, 25, 30]
dimenr = [10, 15, 20, 25, 30]
dimenn = [10, 15, 20, 25, 30]
tempos1 = []
tempos2 = []
for i in range (len(dimenm)):
    m = dimenm[i]
    for j in range(len(dimenr)):
        r = dimenr[j]
        for k in range(len(dimenn)):
            n = dimenn[k]
            A = np.random.rand(m,r)
            B = np.random.rand(r,n)
            

            def multiplica_lenta (A, B, m, r, n):
                C1 = np.zeros(shape =(m,n), dtype=np.float64)
                for i in range(m):
                    for j in range(r):
                        for k in range(n):
                            C1[i,k] += A[i,j]*B[j,k]
                return C1

            tinicial = time.time()
            C1 = multiplica_lenta (A, B, m, r, n)
            tempo_corrido1 = time.time() - tinicial
            
            def multiplica_rapida (A, B, m, r, n):
                C2 = A@B
                return C2

            tinicial = time.time()
            C2 = multiplica_rapida(A, B, m, r, n)
            tempo_corrido2 = time.time() - tinicial

            tempos1.append(tempo_corrido1)
            tempos2.append(tempo_corrido2)



plt.loglog(dimenm, tempos1, '-r')
plt.loglog(dimenm, tempos2, '-g')
plt.xlabel('dimensao')
plt.ylabel('tempos [s]')
plt.title('Grafico dimensao X tempo')
plt.legend(['multiplica_lenta', 'multiplica_rapida'])
plt.grid()
plt.show()


import numpy as np
from animate import animate

dt = 0.1
tempos = np.arange(0, 20, dt)
# G = 6.67408e-11
G = 10

m1 = 4
r1 = np.zeros((len(tempos), 2))
v1 = np.zeros((len(tempos), 2))
a1 = np.zeros((len(tempos), 2))
f1 = np.zeros((len(tempos), 2))

m2 = 1
r2 = np.zeros((len(tempos), 2))
v2 = np.zeros((len(tempos), 2))
a2 = np.zeros((len(tempos), 2))
f2 = np.zeros((len(tempos), 2))

r1[0] = np.array([0, 0])
v1[0] = np.array([0, 0])
a1[0] = np.array([0, 0])
f1[0] = np.array([0, 0])

r2[0] = np.array([8, 8])
v2[0] = np.array([1, -0.5])
a2[0] = np.array([0, 0])
f2[0] = np.array([0, 0])

## calcular f
f1[0] = (G*m1*m2)/np.linalg.norm(r2[0]-r1[0])**3 * (r2[0]-r1[0])
f2[0] = (G*m1*m2)/np.linalg.norm(r1[0]-r2[0])**3 * (r1[0]-r2[0])

## calcular a
a1[0] = f1[0] / m1
a2[0] = f2[0] / m2

solution = np.zeros((len(tempos) - 1, 9))

for i in range(len(tempos)-1):
    ## calcular novo r
    r1[i+1] = r1[i] + v1[i] * dt + (1/2)*a1[i]*dt**2
    r2[i+1] = r2[i] + v2[i] * dt + (1/2)*a2[i]*dt**2

    ## calcular novo f
    f1[i+1] = (G*m1*m2)/np.linalg.norm(r2[i+1]-r1[i+1])**3 * (r2[i+1]-r1[i+1])
    f2[i+1] = (G*m1*m2)/np.linalg.norm(r1[i+1]-r2[i+1])**3 * (r1[i+1]-r2[i+1])

    ## calcular novo a
    a1[i+1] = f1[i+1] / m1
    a2[i+1] = f2[i+1] / m2

    ## calcular novo v
    v1[i+1] = v1[i] + (1/2)*(a1[i] + a1[i+1]) * dt
    v2[i+1] = v2[i] + (1/2)*(a2[i] + a2[i+1]) * dt

    solution[i, :] = tempos[i], r1[i, 0], r1[i, 1], v1[i, 0], v1[i, 1], r2[i, 0], r2[i, 1], v2[i, 0], v2[i, 1]

animate(r1, r2, m1, m2, tempos)
np.savetxt("result.txt", solution)

import numpy as np
from animate import animate
import matplotlib.pyplot as plt

m1 = 4
m2 = 1

def k(m1, m2, v1, v2):
    return (1/2)*m1*np.linalg.norm(v1)**2 + (1/2)*m2*np.linalg.norm(v2)**2

def plot(K, t):
    plt.title("Energia cinética")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Energia (J)")
    plt.scatter(t, K, s=10)
    plt.plot(t, K)
    plt.show()

solutions = np.loadtxt("result.txt")

t  = np.zeros(len(solutions))
r1 = np.zeros((len(solutions), 2))
v1 = np.zeros((len(solutions), 2))
r2 = np.zeros((len(solutions), 2))
v2 = np.zeros((len(solutions), 2))

for i, solution in enumerate(solutions):
    t[i] = solution[0]
    r1[i] = solution[1:3]
    v1[i] = solution[3:5]
    r2[i] = solution[5:7]
    v2[i] = solution[7:9]

# animate(r1, r2, m1, m2, t)

K = np.zeros(len(t))

for i in range(len(t)):
    K[i] = k(m1, m2, v1[i], v2[i])

print(K)
print(t)
plot(K, t)

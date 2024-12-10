import numpy as np
from animate import animate

m1 = 4
m2 = 1

def k(m1, m2, v1, v2):
    return (1/2)*m1*v1**2 + (1/2)*m2*v2**2

# t, r1, r2, v1, v2 = np.loadtxt("result.txt")
solutions = np.loadtxt("result.txt")

t  = np.zeros(len(solutions))
r1 = np.zeros((len(solutions), 2))
v1 = np.zeros((len(solutions), 2))
r2 = np.zeros((len(solutions), 2))
v2 = np.zeros((len(solutions), 2))

# t = solutions[:, 0]
# r1 = solutions[:, 1:2]
# v1 = solutions[:, 3:4]
# r2 = solutions[:, 5:6]
# v2 = solutions[:, 7:8]

for i, solution in enumerate(solutions):
    t[i] = solution[0]
    r1[i] = solution[1:3]
    v1[i] = solution[3:5]
    r2[i] = solution[5:7]
    v2[i] = solution[7:9]

animate(r1, r2, m1, m2, t)

# animate(r1, r2, m1, m2, t)

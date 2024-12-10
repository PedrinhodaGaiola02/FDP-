import numpy as np
from animate import animate

m1 = 4
m2 = 1

def k(m1, m2, v1, v2):
    return (1/2)*m1*v1**2 + (1/2)*m2*v2**2

# t, r1, r2, v1, v2 = np.loadtxt("result.txt")
solutions = np.loadtxt("result.txt")

t = solutions[:, 0]
r1 = solutions[:, 1:2]
v1 = solutions[:, 3:4]
r2 = solutions[:, 5:6]
v2 = solutions[:, 7:8]

animate(r1, r2, m1, m2, t)

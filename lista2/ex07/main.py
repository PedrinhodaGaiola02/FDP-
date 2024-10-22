from matplotlib import pyplot as plt

from domain import r
from graphic import plot
from mpl_toolkits.mplot3d import Axes3D

viagem = r(10000)
plot(viagem)

plt.plot(-50, 50, 50)
plt.plot(50, -50, 50)
plt.plot(50, 50, -50)
plt.plot(-50, -50, 50)
plt.plot(-50, -50, -50)
plt.plot(50, 50, 50)
plt.show()
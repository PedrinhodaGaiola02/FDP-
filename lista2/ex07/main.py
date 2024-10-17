from matplotlib import pyplot as plt

from domain import r
from graphic import plot

viagem = r(10000)
plot(viagem)

plt.plot(-50, 50)
plt.plot(50, -50)
plt.plot(50, 50)
plt.plot(-50, -50)
plt.show()
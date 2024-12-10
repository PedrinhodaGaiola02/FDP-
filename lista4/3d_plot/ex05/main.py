import numpy as np
from matplotlib import pyplot as plt

def f(x, y):
    return np.cos(x) * np.sin(y)

def dfdx(x, y):
    return -np.sin(x) * np.sin(y)

def dfdy(x, y):
    return np.cos(x) * np.cos(y)

x, y = np.meshgrid(np.linspace(-np.pi, np.pi, 20), np.linspace(-np.pi, np.pi, 20))
z = f(x, y)

u = dfdx(x, y)
v = dfdy(x, y)

fig = plt.figure()

plt.style.use('_mpl-gallery-nogrid')

ax = fig.add_subplot(221, projection='3d')
ax.set_title("3D")
ax.plot_surface(x, y, z)

ax2 = fig.add_subplot(222)
ax2.set_title("Curvas de nível")
ax2.contourf(x, y, z, 10)

ax3 = fig.add_subplot(223)
ax3.set_title("Quiver")
ax3.quiver(x, y, u, v)

ax4 = fig.add_subplot(224)
ax4.set_title("Quiver + Curvas de nível")
ax4.contourf(x, y, z, 10)
ax4.quiver(x, y, u, v, width=0.002)

plt.show()

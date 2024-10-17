import numpy as np
from matplotlib import pyplot as plt
from equations import f

ax = plt.axes(projection="3d")

x_domain = np.linspace(-1, 1, 2000)
y_domain = np.linspace(-1, 1, 2000)

x, y = np.meshgrid(x_domain, y_domain)
z = f(x, y)

ax.contour3D(x, y, z, 150, cmap="binary", alpha=0.3)
ax.contour3D(x, y, -z, 150, cmap="binary", alpha=0.3)

ax.set_title('Symmetric Contour Plot', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('X Axis', fontsize=12, labelpad=10)
ax.set_ylabel('Y Axis', fontsize=12, labelpad=10)
ax.set_zlabel('Z Axis', fontsize=12, labelpad=10)

ax.view_init(elev=30, azim=45)
plt.tight_layout()
plt.show()

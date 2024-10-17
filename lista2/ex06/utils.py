import numpy as np
from matplotlib import pyplot as plt

def monte_carlo(number_of_points, label="Estimando área via método de Monte Carlo..."):
    points = np.random.uniform(-1, 1, (number_of_points, 3))

    distances_squared = np.sum(points**2, axis=1)
    inside_mask = distances_squared < 1

    inside = points[inside_mask]
    outside = points[~inside_mask]

    retangle_volume = 8
    figure_volume = (len(inside) / number_of_points) * retangle_volume

    return figure_volume, np.array(inside), np.array(outside)

def draw_sphere(ax):
    theta = np.linspace(0, np.pi, 20)
    phi = np.linspace(0, 2 * np.pi, 20)

    theta, phi = np.meshgrid(theta, phi)

    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    ax.plot_surface(x, y, z, cmap="binary", alpha=0.3)

    ax.set_title('Sphere Surface', fontsize=16, fontweight='bold', pad=20)

    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_zticks([-1, 0, 1])

    ax.set_xlabel('X Axis', fontsize=12, labelpad=10)
    ax.set_ylabel('Y Axis', fontsize=12, labelpad=10)
    ax.set_zlabel('Z Axis', fontsize=12, labelpad=10)

    plt.tight_layout()

def scatter(ax, inside, outside):
    ax.scatter(inside[:,0], inside[:,1], inside[:,2], c="blue", s=0.1)
    ax.scatter(outside[:,0], outside[:,1], outside[:,2], c="gray", s=0.1)
    pass

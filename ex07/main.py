import numpy as np
from matplotlib import pyplot as plt, animation
from life import grid_update
from life import count_borderers

N = 100
p0, p1 = 0.8, 0.2

grid = np.random.choice([0, 1], N*N, p=[p0, p1]).reshape(N, N)

def update(frameNum, img, grid):
    grid = grid_update(grid)

    plt.title(f"Game of Life - Frame {frameNum}")
    return ax.imshow(grid, interpolation='nearest')

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')

ani = animation.FuncAnimation(fig, update, fargs=(img, grid,), cache_frame_data=False, interval=200)
plt.show()

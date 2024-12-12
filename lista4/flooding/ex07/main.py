import numpy as np
from matplotlib import pyplot as plt, animation
from copy import deepcopy

N = 100
p = 0.6

if (N % 2 == 0):
    N += 1

grid = np.random.choice([0, 2], N*N, p=[p, 1-p]).reshape(N, N)
grid[N//2][N//2] = 1

def update_grid(grid):
    old_grid = deepcopy(grid)

    for line in range(len(old_grid)):
        for column in range(len(old_grid[line])):
            if old_grid[line, column] == 1:
                if line > 0 and old_grid[line - 1, column] != 2:
                    grid[line-1, column] = 1

                if line < len(old_grid) - 1 and old_grid[line+1, column] != 2:
                    grid[line+1, column] = 1

                if column > 0 and old_grid[line, column-1] != 2:
                    grid[line, column-1] = 1

                if column < len(old_grid[line]) - 1 and old_grid[line, column+1] != 2:
                    grid[line, column+1] = 1

    return grid


def update(frame_num, grid):
    grid = update_grid(grid)

    plt.title(f"Flooding Algorithm - Frame {frame_num}")
    return ax.imshow(grid, interpolation='nearest', cmap='Blues')

fig, ax = plt.subplots()
designer = ax.imshow(grid, interpolation='nearest', cmap='Blues')

ani = animation.FuncAnimation(
    fig,
    update,
    fargs=(grid,),
    cache_frame_data=False,
    interval=200,
)
plt.show()

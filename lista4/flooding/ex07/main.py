import numpy as np

N = 10
p = 0.5

if (N % 2 == 0):
    N += 1

grid = np.random.choice([0, 2], N*N, p=[p, 1-p]).reshape(N, N)
grid[N//2][N//2] = 1

def update(grid):
    def flood(line, column, grid):
        
    
    for line in range(len(grid)):
        for column in range(len(grid[line])):
            grid = flood(line, column, grid)
    return grid

print(grid)

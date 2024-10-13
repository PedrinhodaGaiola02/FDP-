from copy import deepcopy

## Regras:

# 1. Qualquer célula viva com menos de dois vizinhos vivos morre
# 2. Qualquer célula viva com dois ou três vizinhos vivos continua viva para a próxima geração
# 3. Qualquer célula viva com mais de três vizinhos vivos morre
# 4. Qualquer célula morta com exatamente três vizinhos vivos torna-se uma célula viva

def count_borderers(x, y, grid):
    around = (
        (x, y - 1),
        (x, y + 1),

        (x - 1, y),
        (x - 1, y - 1),
        (x - 1, y + 1),

        (x + 1, y),
        (x + 1, y - 1),
        (x + 1, y + 1),
    )

    # remove celulas que nao existem
    around = tuple(
        filter(lambda cell: cell[0] >= 0 and cell[1] >= 0, around)
    )

    around = tuple(
        filter(lambda cell: cell[0] < len(grid) and cell[1] < len(grid[0]), around)
    )

    count = 0
    for (x, y) in around:
        if grid[x][y] == 1:
            count += 1

    return count

def grid_update(grid):
    old_grid = deepcopy(grid)

    for line in range(len(grid)):
        for column in range(len(grid[line])):
            borderers = count_borderers(line, column, old_grid)

            if borderers < 2 or borderers > 3:
                grid[line][column] = 0
            if borderers == 3:
                grid[line][column] = 1

    return grid



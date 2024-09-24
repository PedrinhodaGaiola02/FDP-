
## Regras:

# 1. Qualquer célula viva com menos de dois vizinhos vivos morre
# 2. Qualquer célula viva com dois ou três vizinhos vivos continua viva para a próxima geração
# 3. Qualquer célula viva com mais de três vizinhos vivos morre
# 4. Qualquer célula morta com exatamente três vizinhos vivos torna-se uma célula viva

def count_borderers(x, y, grid):
    around = (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1)
    )

    count = 0

    for (x, y) in around:
        if x < 0 or y < 0 or x > len(grid) - 1 or y > len(grid[0]) - 1:
            continue

        if grid[x][y] == 1:
            count += 1

    return count

def grid_update(grid):
    new_grid = grid

    for line in range(len(grid)):
        for column in range(len(grid[line])):
            borderers = count_borderers(line, column, grid)

            if borderers < 2 or borderers > 3:
                new_grid[line][column] = 0
            if borderers == 3:
                print('ressuscitando: ', line, column)
                new_grid[line][column] = 1

    print(new_grid[0])
    return new_grid



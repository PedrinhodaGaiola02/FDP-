import numpy as np

possibilities = (
    np.array((1, 0, 0)),   # +X (direita)
    np.array((0, 1, 0)),   # +Y (frente)
    np.array((0, 0, 1)),   # +Z (cima)
    np.array((-1, 0, 0)),  # -X (esquerda)
    np.array((0, -1, 0)),  # -Y (trás)
    np.array((0, 0, -1))   # -Z (baixo)
)

def walk(size=1):
    next_step = possibilities[np.random.randint(0, 6)] * size
    return next_step


def r(t, previous_travel=[np.array((0,0,0))]):
    travel = list(previous_travel)

    for i in range(t):
        travel.append(np.array(travel[-1]) + walk())

    return np.array(travel)

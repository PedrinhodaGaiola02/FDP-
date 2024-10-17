import numpy as np

possibilities = (
    np.array((1, 0)),
    np.array((0, 1)),
    np.array((-1, 0)),
    np.array((0, -1)),
)

def walk(size=1):
    next_step = possibilities[np.random.randint(0, 4)] * size
    return np.array(next_step)

def r(t, previous_travel=[np.array((0,0))]):
    travel = list(previous_travel)

    for i in range(t):
        travel.append(travel[-1] + walk())

    return np.array(travel)

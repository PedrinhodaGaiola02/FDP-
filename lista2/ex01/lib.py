
import numpy as np

def jogar_dados(numero):
    return tuple(
        np.random.randint(1, 7, size=numero)
    )

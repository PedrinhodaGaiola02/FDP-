import numpy as np

def f(x):
    return x * np.exp(-(x**2)) - 0.1

def df(x):
    return (1 - 2*x**2) * np.exp(-(x**2))
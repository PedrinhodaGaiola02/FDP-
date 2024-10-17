from numpy import sqrt

def f(x, y, radius=1):
    return sqrt(radius ** 2 - x**2 - y**2)

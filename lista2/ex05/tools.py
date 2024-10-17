import numpy as np
from math import pi
from progress.bar import Bar

def image(function, domain):
    return tuple(map(function, domain))

def monte_carlo(f, g, h, j, number_of_points):
    points = np.random.uniform((-2, 0), (8, 4), (number_of_points, 2))

    inside = []
    outside = []

    bar = Bar("Estimando área via método de Monte Carlo...", max=number_of_points)
    for (x, y) in points:
        if ((f(x) < y and g(x) > y) or (x < 0 or x > 2*pi)) and ((h(y) < x and j(y) > x) or ((y < 1 or y > g(x)) and (x > 0 and x < 2*pi))):
            inside.append((x, y))
        else:
            outside.append((x, y))

        bar.next()
    print()

    retangle_area = 9 * 4
    figure_area = (len(inside) / number_of_points) * retangle_area

    return figure_area, np.array(inside), np.array(outside)


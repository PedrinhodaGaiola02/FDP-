import numpy as np
from math import pi
from progress.bar import Bar

def image(function, domain):
    return tuple(map(function, domain))

def monte_carlo(f, g, domain, number_of_points):
    points = np.random.uniform((domain[0], 0), (domain[-1], 4), (number_of_points, 2))

    inside = []
    outside = []

    bar = Bar("Estimando área via método de Monte Carlo...", max=number_of_points)
    for (x, y) in points:
        if f(x) < y and g(x) > y:
            inside.append((x, y))
        else:
            outside.append((x, y))

        bar.next()
    print()

    retangle_area = 4 * domain[-1]
    figure_area = (len(inside) / number_of_points) * retangle_area

    return figure_area, np.array(inside), np.array(outside)

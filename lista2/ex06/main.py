from pandas import DataFrame
from matplotlib import pyplot as plt
from utils import draw_sphere, scatter, monte_carlo

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

draw_sphere(ax)
volume, dentro, fora = monte_carlo(1000)
scatter(ax, dentro, fora)

plt.show()

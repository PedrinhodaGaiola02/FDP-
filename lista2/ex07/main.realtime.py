from matplotlib import pyplot as plt, animation
from domain import r

fig, ax = plt.subplots()

desenho = ax.plot(0, 0)[0]
travel = r(0)

def update(frameNum, travel):
    travel = r(1, previous_travel=travel)

    desenho.set_xdata(travel[:,0])
    desenho.set_ydata(travel[:,1])

    # plt.title(f"Walker - Step:", frameNum)
    return desenho, travel

ani = animation.FuncAnimation(fig, update, interval=200, frames=40, fargs=(travel,))
plt.show()

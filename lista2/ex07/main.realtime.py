from matplotlib import pyplot as plt, animation
from domain import r

fig, ax = plt.subplots()

desenho = ax.plot(0, 0)[0]

ax.set(
    xlim=[-50, 50],
    ylim=[-50, 50],
    xlabel="X Axis",
    ylabel="Y Axis",
)

travel = r(0)

def update(frameNum):
    global travel
    travel = r(frameNum, previous_travel=travel)

    desenho.set_xdata(travel[:,0])
    desenho.set_ydata(travel[:,1])

    plt.title("Walker - Step: {}".format(frameNum))
    return (desenho, travel)

ani = animation.FuncAnimation(fig, update, interval=200, frames=50)
plt.show()

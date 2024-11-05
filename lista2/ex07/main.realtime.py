from matplotlib import pyplot as plt, animation
from domain import r

fig, ax = plt.subplots()

desenho = ax.plot(0, 0)[0]

ax.set(
    xlim=[-100, 100],
    ylim=[-100, 100],
    xlabel="X Axis",
    ylabel="Y Axis",
)

travel = r(0)

def update(frame):
    global travel

    if (frame == 0): travel = r(0)

    travel = r(frame, previous_travel=travel)

    desenho.set_xdata(travel[:,0])
    desenho.set_ydata(travel[:,1])

    plt.title("Walker - Step: {}".format(frame))
    return (desenho, travel)

ani = animation.FuncAnimation(fig, update, interval=100, frames=100)
plt.show()

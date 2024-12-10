import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(r1, r2, m1, m2, tempos):
    global animation
    fig, ax = plt.subplots()

    ax.set_title("Simulação de dois corpos")
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)

    img1 = ax.scatter(r1[0, 0], r1[0, 1], s=10*m1)
    img2 = ax.scatter(r2[:, 0], r2[:, 1], s=10*m2)

    def update(frameNum, img1, img2, r1, r2):
        ax.set_title("Simulação de dois corpos - t={:.2f}s".format(tempos[frameNum]))
        img1.set_offsets(r1[frameNum])
        img2.set_offsets(r2[frameNum])

    animation = animation.FuncAnimation(
        fig,
        update,
        frames=len(tempos),
        fargs=(img1, img2, r1, r2),
        cache_frame_data=False,
        interval=100
    )

    plt.show()
    # animation.save("ex06.gif")


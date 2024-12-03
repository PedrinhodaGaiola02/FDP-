import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image
from matplotlib import animation
import functools

dt = 0.1
tempos = np.arange(0, 10, dt)
G = 6.67408e-11

m1 = 1
r1 = np.zeros((len(tempos), 2))
v1 = np.zeros((len(tempos), 2))
a1 = np.zeros((len(tempos), 2))
f1 = np.zeros((len(tempos), 2))

m2 = 1
r2 = np.zeros((len(tempos), 2))
v2 = np.zeros((len(tempos), 2))
a2 = np.zeros((len(tempos), 2))
f2 = np.zeros((len(tempos), 2))

r1[0] = np.array([0, 0])
v1[0] = np.array([0, 0])
a1[0] = np.array([0, 0])
f1[0] = np.array([0, 0])

r2[0] = np.array([8, 8])
v2[0] = np.array([0, 0])
a2[0] = np.array([0, 0])
f2[0] = np.array([0, 0])

## calcular f
f1[0] = (G*m1*m2)/np.linalg.norm(r2[0]-r1[0])**3 * (r2[0]-r1[0])
f2[0] = (G*m1*m2)/np.linalg.norm(r1[0]-r2[0])**3 * (r1[0]-r2[0])

## calcular a
a1[0] = f1[0] / m1
a2[0] = f2[0] / m2

for i in range(len(tempos)-1):
    ## calcular novo r
    r1[i+1] = r1[i] + r1[i] * v1[i] * dt + (1/2)*a1[i]*dt**2
    r2[i+1] = r2[i] + r2[i] * v2[i] * dt + (1/2)*a2[i]*dt**2

    ## calcular novo f
    f1[i+1] = (G*m1*m2)/np.linalg.norm(r2[i+1]-r1[i+1])**3 * (r2[i+1]-r1[i+1])
    f2[i+1] = (G*m1*m2)/np.linalg.norm(r1[i+1]-r2[i+1])**3 * (r1[i+1]-r2[i+1])

    ## calcular novo a
    a1[i+1] = f1[i+1] / m1
    a2[i+1] = f2[i+1] / m2

    ## calcular novo v# universal gravitation constant
    v1[i+1] = v1[i] + (1/2)*(a1[i] + a1[i+1]) * dt
    v2[i+1] = v2[i] + (1/2)*(a2[i] + a2[i+1]) * dt

# animate
fig, ax = plt.subplots()
line1, = ax.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return line1,

def update(frame, ln, x, y):
    x.append(frame)
    y.append(np.sin(frame))
    ln.set_data(x, y)
    return ln,

ani = animation.FuncAnimation(
    fig, functools.partial(update, ln=line1, x=[], y=[]),
    frames=np.linspace(0, 2*np.pi, 128),
    init_func=init, blit=True)

plt.show()
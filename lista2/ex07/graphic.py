from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot(travel):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(travel[:, 0], travel[:, 1], travel[:, 1])

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    

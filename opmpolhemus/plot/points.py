from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def plot_points(points, pt=0.8, c='b'):
    print('🎨 Making some plots')
    plot_name = 'point plot, #points={}'.format(len(points))
    fig = plt.figure(plot_name)
    ax = fig.add_subplot(111, projection='3d')
    xyz = points
    ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], color=c, s=pt)


def plot_points_list(list_in=[], pt=0.8):
    print('🎨 Making some plots')
    plot_name = 'point plot, #point sets={}'.format(len(list_in))
    fig = plt.figure(plot_name)
    ax = fig.add_subplot(111, projection='3d')
    colors = [plt.cm.tab20b(each) for each in np.linspace(0, 1, len(list_in))]
    for (k, col) in zip(list(range(0, len(list_in))), colors):
        xyz = list_in[k]
        ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], color=col, s=pt)


# if (__name__ == '__main__'):

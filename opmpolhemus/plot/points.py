from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def plot_points(pcl, indices=[], pt=6.0, c='r'):
    print('🎨 Making some plots')
    plot_name = 'point plot, #points={}'.format(len(indices))
    fig = plt.figure(plot_name)
    ax = fig.add_subplot(111, projection='3d')
    if len(indices):
        xyz = np.array(pcl)[np.array(indices)]
    else:
        xyz = np.array(pcl)
    ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], color=c, s=pt)
    if len(indices):
        for i in range(len(indices)):
            ax.text(xyz[i, 0], xyz[i, 1], xyz[i, 2], indices[i])


def plot_points_list(list_in=[], pt=5.8):
    print('🎨 Making some plots')
    plot_name = 'point plot, #point sets={}'.format(len(list_in))
    fig = plt.figure(plot_name)
    ax = fig.add_subplot(111, projection='3d')
    colors = [plt.cm.prism(each) for each in np.linspace(0, 1, len(list_in))]
    for (k, col) in zip(list(range(0, len(list_in))), colors):
        xyz = list_in[k]
        ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], color=col, s=pt)
        ax.text(xyz[0, 0], xyz[0, 1], xyz[0, 2], k, fontsize=12)


# if (__name__ == '__main__'):

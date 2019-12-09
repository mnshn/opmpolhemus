from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def plot_points(pcl,
                indices=[],
                surface_slopes=[],
                projected_points=[],
                additional_points=[],
                pt=6.0,
                c='r'):
    print('🎨 Making some plots')
    plot_name = 'point plot,  # points={}, range: {}-{}'.format(
        len(indices), min(indices), max(indices))
    fig = plt.figure(plot_name)
    ax = fig.add_subplot(111, projection='3d')
    ax.grid(False)
    if len(indices):
        xyz = np.array(pcl)[np.array(indices)]
    else:
        xyz = np.array(pcl)
    ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], color=c, s=pt)
    if len(indices):
        for i in range(len(indices)):
            ax.text(xyz[i, 0], xyz[i, 1], xyz[i, 2], indices[i])
    if (len(surface_slopes)):
        a = surface_slopes[0]
        b = surface_slopes[1]
        c = surface_slopes[2]
        xMax = max(xyz[:, 0])
        xMin = min(xyz[:, 0])
        yMax = max(xyz[:, 1])
        yMin = min(xyz[:, 1])

        def f(x, y):
            return a * x + b * y + c

        x = np.linspace(xMin, xMax, 30)
        y = np.linspace(yMin, yMax, 30)

        X, Y = np.meshgrid(x, y)
        Z = f(X, Y)
        ax.contour3D(X, Y, Z, 50, cmap='binary')
    if (len(projected_points)):
        pxyz = np.array(projected_points)
        ax.scatter(pxyz[:, 0], pxyz[:, 1], pxyz[:, 2], color='b')

    if (len(additional_points)):
        axyz = np.array(additional_points)
        ax.scatter(axyz[:, 0], axyz[:, 1], axyz[:, 2], color='m')


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


def plane_plot(points):
    plot_name = 'point plot, point0={}'.format(points[0])
    xy = np.array(points)
    minor_xticks = np.arange(2 * min(xy[:, 0]), 2 * max(xy[:, 0]), 0.001)
    minor_yticks = np.arange(2 * min(xy[:, 1]), 2 * max(xy[:, 1]), 0.001)
    major_xticks = np.arange(2 * min(xy[:, 0]), 2 * max(xy[:, 0]), 0.01)
    major_yticks = np.arange(2 * min(xy[:, 1]), 2 * max(xy[:, 1]), 0.01)
    fig = plt.figure(plot_name)
    ax = fig.add_subplot(111)
    ax.set_xticks(minor_xticks, minor=True)
    ax.set_yticks(minor_yticks, minor=True)
    ax.set_xticks(major_xticks)
    ax.set_yticks(major_yticks)
    ax.scatter(xy[:, 0], xy[:, 1])
    ax.grid(which='minor')
    ax.grid(which='major', alpha=1, color='m')
    ax.axis('equal')


# if (__name__ == '__main__'):

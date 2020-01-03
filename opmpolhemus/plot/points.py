from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def axisEqual3D(ax):
    extents = np.array(
        [getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    sz = extents[:, 1] - extents[:, 0]
    centers = np.mean(extents, axis=1)
    maxsize = max(abs(sz))
    r = maxsize / 2
    for ctr, dim in zip(centers, 'xyz'):
        getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)


def plot_points(pcl,
                indices=[],
                surface_slopes=[],
                projected_points=[],
                additional_points=[],
                pt=6.0,
                c='r',
                name_label=''):
    plot_name = f'point plot {name_label}'
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
    axisEqual3D(ax)


def plot_points_list(list_in=[], pt=3.0, name_label='', additional_points=[]):
    plot_name = 'point plot {}, #point sets={}'.format(name_label,
                                                       len(list_in))
    fig = plt.figure(plot_name)
    ax = fig.add_subplot(111, projection='3d')
    colors = [plt.cm.prism(each) for each in np.linspace(0, 1, len(list_in))]
    for (k, col) in zip(list(range(0, len(list_in))), colors):
        xyz = list_in[k]
        ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], color=col, s=pt)
        ax.text(xyz[0, 0], xyz[0, 1], xyz[0, 2], k, fontsize=12)
    if len(additional_points):
        axyz = np.array(additional_points)
        ax.scatter(axyz[:, 0], axyz[:, 1], axyz[:, 2], color='r', s=6.0)
    axisEqual3D(ax)


def frame_plot(points, frame_points=[], additional_points=[], name_label=''):
    plot_name = 'point plot {}'.format(name_label)
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
    ax.grid(which='major', alpha=0.7, color='k')
    ax.axis('equal')
    if len(frame_points):
        fxy = np.array(frame_points)
        ax.scatter(fxy[:, 0], fxy[:, 1])
    if len(additional_points):
        axy = np.array(additional_points)
        ax.scatter(axy[:, 0], axy[:, 1])


# if (__name__ == '__main__'):

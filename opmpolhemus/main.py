from utils.parser import mat_parser
from plot.points import plot_points
from handlers.kd_tree import neighbors, query_sphere, query_shell
import matplotlib.pyplot as plt

import scipy.spatial as ss
import numpy as np
VOLUME_CUT_OFF = 10e-7
SHELL_CUT_OFF = 0.001
test_file = '../db/point.txt'

opm_points = mat_parser(test_file)

# opm1 = opm_points[152:160]
opm1 = opm_points
plot_points(opm1)
# plot_points(opm_points[np.array([152, 480, 477, 216])])

delta1 = np.linalg.norm(opm1[4] - opm1[3])
delta2 = np.linalg.norm(opm1[4] - opm1[0])


def point_giver(p):
    return np.unique(
        np.concatenate((query_shell(opm_points, [p],
                                    radius=delta1,
                                    delta=SHELL_CUT_OFF),
                        query_shell(opm_points, [p],
                                    radius=delta2,
                                    delta=SHELL_CUT_OFF))))


def walker(index, steps=4, w=0):
    out = []
    ps = point_giver(opm_points[index])
    for i in ps:
        psi = point_giver(opm_points[i])
        for j in psi:
            psij = point_giver(opm_points[j])
            for k in psij:
                psijk = point_giver(opm_points[k])
                if index in psijk and len(list(set([index, i, j, k
                                                    ]))) == steps:
                    plane = opm_points[np.array([index, i, j, k])]
                    hull = ss.ConvexHull(plane)
                    if hull.volume < 1e-9:
                        out.extend(list(set([index, i, j, k])))
    # plot_points()
    plot_points(opm_points[np.array(out)])


i = 0


def round_trip(index, i=0, steps=3, pcl=opm_points):
    if i < steps:
        i += 1
        for j in neighbors(pcl, index):
            print(i, index, neighbors(pcl, index), j,
                  neighbors(pcl, j, prev=index, top=5))
            round_trip(j, i)


round_trip(152)

# walker(152)
# plt.show()

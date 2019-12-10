from utils.parser import mat_parser

from plot.points import plot_points, plot_points_list, plane_plot

from cluster.clusters import cluster_opms
from cluster.process import post_process

from fitframe.plane import plane_maker
from fitframe.projection import affine_trafo
from fitframe.fit import FRAME_POINTS, fitter, rotate_frame

import numpy as np
import matplotlib.pyplot as plt

ANGLE_MESH = 0.1

test_file = '../db/point.txt'

opm_raw = mat_parser(test_file)

all_opms = post_process(cluster_opms(opm_raw), opm_raw)

for i in range(0, 5):
    slopes, projections = plane_maker(all_opms[i])
    plane_points = affine_trafo(slopes, projections)
    error, angle = fitter(plane_points, ANGLE_MESH)
    plane_plot(plane_points, frame_points=rotate_frame(FRAME_POINTS, angle))

    # plot_points(opm,
    #             indices=single_opm(i),
    #             surface_slopes=slopes,
    #             projected_points=projections,
    #             additional_points=[])


def opm_list():
    out = []
    for i in list(all_opms.keys()):
        out.append(np.array(all_opms[i]))
    return np.array(out)


plot_points_list(opm_list())

plt.show()

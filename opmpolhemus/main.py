from utils.parser import mat_parser
from plot.points import plot_points, plot_points_list, plane_plot
from handlers.clusters import cluster_opms
from handlers.plane import plane_maker
from handlers.post_process import post_process
from handlers.projection import affine_trafo

from fitframe.fit import FRAME_POINTS, fitter, rotate_frame

import numpy as np
import matplotlib.pyplot as plt

ANGLE_MESH = 0.1

test_file = '../db/point.txt'

opm_raw = mat_parser(test_file)
all_opms = cluster_opms(opm_raw)


def single_opm(i):
    return list(post_process(all_opms, opm_raw)[i].values())


for i in range(19, 23):
    slopes, projections = plane_maker(single_opm(i))
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
        out.append(np.array(single_opm(i)))
    return np.array(out)


plot_points_list(opm_list())

plt.show()

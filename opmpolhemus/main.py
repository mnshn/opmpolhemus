from utils.parser import mat_parser
from plot.points import plot_points, plot_points_list, plane_plot
from handlers.clusters import cluster_opms
from handlers.plane import plane_maker
from handlers.post_process import post_process
from handlers.projection import affine_trafo

from fitframe.fit import FRAME_POINTS, fitter

import numpy as np
import matplotlib.pyplot as plt

DOUBLE_CLICK_THRESHOLD = 10e-4

test_file = '../db/point.txt'

opm_raw = mat_parser(test_file)
all_opms = cluster_opms(opm_raw)


def single_opm(i):
    return list(post_process(all_opms, opm_raw)[i].values())


for i in range(0, 1):
    slopes, projections = plane_maker(single_opm(i))
    plane_points = affine_trafo(slopes, projections)
    plane_plot(plane_points, frame_points=FRAME_POINTS)
    fitter(plane_points)
    # plot_points(opm,
    #             indices=single_opm(i),
    #             surface_slopes=slopes,
    #             projected_points=projections,
    #             additional_points=[])

# def opm_list():
#     out = []
#     for i in list(all_opms.keys()):
#         out.append(np.array(list(map(lambda x: opm[x], single_opm(i)))))
#     return np.array(out)

# plot_points_list(opm_list())

# plt.show()

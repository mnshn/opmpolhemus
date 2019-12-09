from utils.parser import mat_parser
from plot.points import plot_points, plot_points_list, plane_plot
from handlers.clusters import opms
from handlers.plane import plane_maker, post_process
from handlers.fit_rectangle import affine_trafo

import numpy as np
import matplotlib.pyplot as plt

DOUBLE_CLICK_THRESHOLD = 10e-4

test_file = '../db/point.txt'

opm = mat_parser(test_file)
all_opms = opms(opm)


def single_opm(i):
    return list(post_process(all_opms, opm)[i].values())


for i in range(0, 4):
    slopes, projections = plane_maker(single_opm(i))
    plane_plot(affine_trafo(slopes, projections)[:-1])
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

plt.show()

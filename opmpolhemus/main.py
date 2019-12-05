from utils.parser import mat_parser
from plot.points import plot_points, plot_points_list
# from handlers.kd_tree import neighbors, query_sphere, query_shell
from handlers.looper import looper
from handlers.fit import gradOfCost, gradDescent
from handlers.fit_sci import plane_maker

import matplotlib.pyplot as plt
import numpy as np

DOUBLE_CLICK_THRESHOLD = 10e-4

test_file = '../db/point.txt'

opm = mat_parser(test_file)
opms = looper(opm)


def single_opm(i):
    return list(x for y in list(opms[i].values()) for x in y)


# print(plane_maker(single_opm(0), opm))
plot_points(opm,
            indices=single_opm(0),
            surface_slopes=plane_maker(single_opm(0), opm))

# def opm_list():
#     out = []
#     for i in list(opms.keys()):
#         out.append(np.array(list(map(lambda x: opm[x], single_opm(i)))))
#     return np.array(out)

# plot_points_list(opm_list())

plt.show()
print(gradDescent(single_opm(0), opm))

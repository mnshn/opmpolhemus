from utils.parser import mat_parser
from plot.points import plot_points, plot_points_list
from handlers.clusters import opms
from handlers.fit import plane_maker

import numpy as np
import matplotlib.pyplot as plt

DOUBLE_CLICK_THRESHOLD = 10e-4

test_file = '../db/point.txt'

opm = mat_parser(test_file)
all_opms = opms(opm)


def single_opm(i):
    return list(x for y in list(all_opms[i].values()) for x in y)


for i in range(0, 4):
    plot_points(opm,
                indices=single_opm(i),
                surface_slopes=plane_maker(single_opm(i), opm))


def opm_list():
    out = []
    for i in list(all_opms.keys()):
        out.append(np.array(list(map(lambda x: opm[x], single_opm(i)))))
    return np.array(out)


plot_points_list(opm_list())

plt.show()

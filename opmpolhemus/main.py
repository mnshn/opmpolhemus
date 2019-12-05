from utils.parser import mat_parser
from plot.points import plot_points, plot_points_list
# from handlers.kd_tree import neighbors, query_sphere, query_shell
from handlers.looper import looper

import matplotlib.pyplot as plt
import numpy as np
DOUBLE_CLICK_THRESHOLD = 10e-4

test_file = '../db/point.txt'

opm = mat_parser(test_file)
opms = looper(opm)


def single_opm(i):
    return list(x for y in list(opms[i].values()) for x in y)


plot_points(opm, indices=single_opm(0))


def opm_list():
    out = []
    for i in list(opms.keys()):
        out.append(np.array(list(map(lambda x: opm[x], single_opm(i)))))
    return np.array(out)


plot_points_list(opm_list())

plt.show()

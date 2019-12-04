from utils.parser import mat_parser
from plot.points import plot_points
# from handlers.kd_tree import neighbors, query_sphere, query_shell
from handlers.looper import looper

import matplotlib.pyplot as plt

DOUBLE_CLICK_THRESHOLD = 10e-4

test_file = '../db/point.txt'

opm = mat_parser(test_file)

opms = looper(opm)

opm5 = list(range(53, 66))
opm6 = list(range(64, 76))
plot_points(opm, opm5)
# print(opms)
plt.show()

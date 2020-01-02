import numpy as np
import matplotlib.pyplot as plt
from utils.parser import mat_parser
from plot.points import plot_points, plot_points_list, plane_plot

from cluster.clusters import cluster_opms
from cluster.process import post_process

from handler.opm import OPM
from handler.frame import Frame

test_file = '../db/proper02/point.txt'
opm_raw = mat_parser(test_file)

frame_style = 'top'

frame = Frame(frame_style)

plot_style = 'all'


def make_clusters(raw):
    opm_clusters = cluster_opms(raw, frame)
    all_opms = post_process(opm_clusters, raw)
    return all_opms


all_opms = make_clusters(opm_raw)

for i in range(0, 10):
    opm = OPM(all_opms[i], style=frame_style)
    opm.label = i
    opm.show_plane_fit()

# def opm_list():
#     out = []
#     for i in range(0, 31):
#         out.append(np.array(all_opms[i]))
#     return np.array(out)

# def sensor_list():
#     sensors = []
#     for i in range(0, len(all_opms)):
#         opm = OPM(all_opms[i], style=frame_style)
#         sensors.append(opm.sensor)
#     return sensors

# plot_points_list(opm_list(), additional_points=sensor_list())

plt.show()

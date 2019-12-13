from utils.parser import mat_parser
from plot.points import plot_points, plot_points_list, plane_plot

from cluster.clusters import cluster_opms
from cluster.process import post_process

from fitframe.fit import fit_all

import matplotlib.pyplot as plt
import numpy as np

test_file = '../db/proper01/point.txt'
opm_raw = mat_parser(test_file)


def make_clusters(raw):
    opm_clusters = cluster_opms(raw)
    all_opms = post_process(opm_clusters, raw)
    return all_opms


all_opms = make_clusters(opm_raw)
fit_data = fit_all(all_opms)

# for i in range(4, 12):
#     plane_plot(fit_data[i]['plane-points'],
#                frame_points=fit_data[i]['frame-points'],
#                additional_points=fit_data[i]['sensor-points-plane'],
#                name_label=i)

#     ind = list(x for y in list(opm_clusters[i].values()) for x in y)

#     plot_points(opm_raw,
#                 indices=ind,
#                 surface_slopes=fit_data[i]['slopes'],
#                 projected_points=fit_data[i]['projected-points'],
#                 additional_points=fit_data[i]['sensor-points-3d'],
#                 name_label=i)


def opm_list():
    out = []
    for i in list(all_opms.keys()):
        out.append(np.array(all_opms[i]))
    return np.array(out)


def sensor_list():
    sensors = []
    for i in list(all_opms.keys()):
        sensors.append(fit_data[i]['sensor-points-3d'])
    sensors = np.array(list(x for y in sensors for x in y))
    return sensors


plot_points_list(opm_list(), additional_points=sensor_list())

plt.show()

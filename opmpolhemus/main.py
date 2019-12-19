import numpy as np
import matplotlib.pyplot as plt
from utils.parser import mat_parser
from plot.points import plot_points, plot_points_list, plane_plot

from cluster.clusters import cluster_opms
from cluster.process import post_process

from handler.opm import OPM

test_file = '../db/proper02/point.txt'
opm_raw = mat_parser(test_file)

style = 'top'


def make_clusters(raw):
    opm_clusters = cluster_opms(raw)
    all_opms = post_process(opm_clusters, raw)
    return all_opms


all_opms = make_clusters(opm_raw)

for i in range(0, 15):
    opm = OPM(all_opms[i], style)
    # plane_plot(opm.plane_points()[0],
    #            frame_points=opm.frame_fit(),
    #            additional_points=opm.sensor_plane(),
    #            name_label=i)

    ind = list(x for y in list(cluster_opms(opm_raw)[i].values()) for x in y)
    plot_points(opm_raw,
                indices=ind,
                surface_slopes=opm.slopes,
                projected_points=opm.projections,
                additional_points=[opm.sensor],
                name_label=i)

# def opm_list():
#     out = []
#     for i in range(0, 1):
#         out.append(np.array(all_opms[i]))
#     return np.array(out)

# def sensor_list():
#     sensors = []
#     for i in range(0, 1):
#         opm = OPM(all_opms[i], style=style)
#         sensors.append(opm.sensor())
#     return sensors

# plot_points_list(opm_list(), additional_points=sensor_list())

plt.show()

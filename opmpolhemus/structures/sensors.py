import numpy as np

from opmpolhemus.cluster.clusters import cluster_opms
from opmpolhemus.cluster.process import post_process

from opmpolhemus.structures.frame import Frame
from opmpolhemus.structures.opm import OPM

from opmpolhemus.plot.points import plot_points_list

import matplotlib.pyplot as plt


class Sensors():
    def __init__(self, data, frame_style, log_level=0):
        self.frame = Frame(frame_style)
        clusters = cluster_opms(data, self.frame)
        self.clusters = post_process(clusters, data)
        self.order = np.shape(self.clusters)[0]
        self.opms = list(
            OPM(cluster, frame_style) for cluster in self.clusters)
        self.sensors = list(opm.sensor for opm in self.opms)
        self.normals = list(opm.normal for opm in self.opms)
        if log_level == 1:
            print(f'Found {self.order} opms')

    def show_sensors(self):
        plot_points_list(np.array(self.clusters),
                         additional_points=self.sensors,
                         normals=self.normals)
        plt.show()

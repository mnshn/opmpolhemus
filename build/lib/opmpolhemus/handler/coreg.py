import numpy as np

from opmpolhemus.cluster.clusters import cluster_opms
from opmpolhemus.cluster.process import post_process

from opmpolhemus.handler.frame import Frame
from opmpolhemus.handler.opm import OPM

from opmpolhemus.plot.points import plot_points_list

import matplotlib.pyplot as plt


class CoReg():
    def __init__(self, data, frame_stlye, log_level=0):
        self.frame = Frame(frame_stlye)
        clusters = cluster_opms(data, self.frame)
        self.clusters = post_process(clusters, data)
        self.order = np.shape(self.clusters)[0]
        self.opms = list(OPM(x, frame_stlye) for x in self.clusters)
        self.sensors = list(opm.sensor for opm in self.opms)
        if log_level == 1:
            print(f'Found {self.order} opms')

    def show_coreg(self):
        plot_points_list(np.array(self.clusters),
                         additional_points=self.sensors)
        plt.show()

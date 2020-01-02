import math
import numpy as np
from fitframe.plane import plane_maker
from fitframe.projection import affine_trafo
from fitframe.fit import fitter
from constants import Constants
from .frame import Frame

from plot.points import plane_plot


def rotate(point, theta):
    rot_mat = np.array([[math.cos(theta), -math.sin(theta)],
                        [math.sin(theta), math.cos(theta)]])
    return np.matmul(rot_mat, point)


def rotate_frame(set, theta):
    out = []
    for point in set:
        out.append(rotate(point, theta))
    return out


class OPM:
    def __init__(self, data, style='base'):
        frame = Frame(style=style)
        self.data = data
        self.frame = frame
        self.label = None
        self.slopes, self.projections, self.fit_error = plane_maker(data)
        self.plane_points, self.affine_map = affine_trafo(
            self.slopes, self.projections)
        self.frame_fit_angle, self.frame_fit_error = fitter(
            self.plane_points, Constants.ANGLE_FIT_MESH, self.frame.frame)
        self.frame_fit = rotate_frame(self.frame.frame, self.frame_fit_angle)
        self.sensor_plane = rotate_frame([self.frame.sensor[0:2]],
                                         self.frame_fit_angle)
        self.sensor = np.matmul(
            self.affine_map,
            np.append(self.sensor_plane[0], [self.frame.sensor[2], 1]))[0:3]
        self.com = np.matmul(self.affine_map, np.array((0, 0, 0, 1)))[0:3]

    def show_plane_fit(self):
        plane_plot(self.plane_points,
                   frame_points=self.frame_fit,
                   additional_points=self.sensor_plane,
                   name_label=self.label)

    def __repr__(self):
        return 'OPM with com at {}'.format(self.com())

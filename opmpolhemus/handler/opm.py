import math
import numpy as np
from fitframe.plane import plane_maker
from fitframe.projection import affine_trafo
from fitframe.fit import fitter
from constants import Constants
from .frame import Frame


def rotate(point, theta):
    rot_mat = np.array([[math.cos(theta), -math.sin(theta)],
                        [math.sin(theta), math.cos(theta)]])
    return np.matmul(rot_mat, point)


def rotate_frame(set, theta):
    out = []
    for i in set:
        out.append(rotate(i, theta))
    return out


class OPM:
    def __init__(self, data, style='base'):
        frame = Frame(style=style)
        self.data = data
        self.pre_frame = frame
        self.frame = frame.frame
        self.slopes, self.projections, self.fit_error = plane_maker(data)
        self.plane_points, self.affine_map = affine_trafo(
            self.slopes, self.projections)
        self.frame_fit_angle, self.frame_fit_error = fitter(
            self.slopes, Constants.ANGLE_FIT_MESH, self.pre_frame.frame)
        self.frame_fit = rotate_frame(self.frame, self.frame_fit_angle)
        self.sensor_plane = rotate_frame([self.pre_frame.sensor[0:2]],
                                         self.frame_fit_angle)
        self.sensor = np.matmul(
            self.affine_map,
            np.append(self.sensor_plane[0],
                      [self.pre_frame.sensor[2], 1]))[0:3]
        self.com = np.matmul(self.affine_map, np.array((0, 0, 0, 1)))[0:3]

    def __repr__(self):
        return 'OPM with com at {}'.format(self.com())

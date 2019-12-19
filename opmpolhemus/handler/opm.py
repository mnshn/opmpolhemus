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
        frame = Frame(style)
        self.data = data
        self.pre_frame = frame
        self.frame = frame.frame

    # returns (slopes of plane fit, point projections on plane, fit error)
    def plane(self):
        return plane_maker(self.data)

    # returns point (projections in 3d, the affine map used)
    def plane_points(self):
        return affine_trafo(*self.plane()[0:2])

    # returns (the best fit angle of fitting points to frame, fit error)
    def frame_fit_angle(self):
        return fitter(self.plane_points()[0], Constants.ANGLE_FIT_MESH,
                      self.pre_frame.frame)

    # the frame in the plane, rotated by the best angle
    def frame_fit(self):
        return rotate_frame(self.frame, self.frame_fit_angle()[1])

    # the sensor point in 2D
    def sensor_plane(self):
        return rotate_frame([self.pre_frame.sensor[0:2]],
                            self.frame_fit_angle()[1])

    # returns the sensor point in 3D
    def sensor(self):
        return np.matmul(
            self.plane_points()[1],
            np.append(self.sensor_plane()[0],
                      [self.pre_frame.sensor[2], 1]))[0:3]

    def com(self):
        return np.matmul(self.plane_points()[1], np.array((0, 0, 0, 1)))[0:3]

    def __repr__(self):
        return 'OPM with com at {}'.format(self.com())

import math
import numpy as np
from fitframe.plane import plane_maker
from fitframe.projection import affine_trafo
from fitframe.fit import fitter
from constants import Constants
from .frame import Frame
import sys
sys.path.append("..")


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
        slopes, projections, plane_fit_error = plane_maker(data)
        plane_points, affine_map = affine_trafo(slopes, projections)
        frame_fit_error, angle = fitter(plane_points, Constants.ANGLE_FIT_MESH,
                                        frame.frame)
        sensor_points_plane = rotate_frame([frame.sensor[0:2]], angle)
        sensor_points_space = list(
            map(
                lambda x: np.matmul(affine_map,
                                    np.append(x, [frame.sensor[2], 1]))[0:3],
                sensor_points_plane))
        sensor_points_frame_3d = list(
            map(lambda x: np.matmul(affine_map, np.append(x, [0, 1]))[0:3],
                sensor_points_plane))
        frame_center_of_mass = np.matmul(affine_map, np.array(
            (0, 0, 0, 1)))[0:3]
        self.slopes = slopes
        self.projections = projections
        self.plane_points = plane_points
        self.sensor_space = sensor_points_space
        self.sensor_plane = sensor_points_plane
        self.frame = rotate_frame(frame.frame, angle)
        self.com = frame_center_of_mass
        self.sensor_points_frame = sensor_points_frame_3d

    def __repr__(self):
        return 'OPM with com at {}'.format(self.com)

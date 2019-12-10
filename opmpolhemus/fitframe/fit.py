import math
import numpy as np

from .plane import plane_maker
from .projection import affine_trafo

DELTA = 0.0010
RIDGE = 0.0025
XSIZE = 0.0062
YSIZE = 0.0083
YCELL = 0.0019

ANGLE_MESH = 0.1

FRAME_POINTS = [(RIDGE + DELTA, YSIZE + DELTA), (XSIZE + DELTA, RIDGE + DELTA),
                (XSIZE + DELTA, -(RIDGE + DELTA)),
                (RIDGE + DELTA, -(YSIZE + DELTA)),
                (-(RIDGE + DELTA), -(YSIZE + DELTA)),
                (-(XSIZE + DELTA), -(RIDGE + DELTA)),
                (-(XSIZE + DELTA), (RIDGE + DELTA)),
                (-(RIDGE + DELTA), YSIZE + DELTA)]

SENSOR_POINTS = [(0.0, YCELL), (0.0, -YCELL)]
SENSOR_Z = 0.005


def nearest(point, set):
    order = []
    set = np.array(set)
    for i in set:
        order.append(np.linalg.norm(point - i))
    return min(order)


def rotate(point, theta):
    rot_mat = np.array([[math.cos(theta), -math.sin(theta)],
                        [math.sin(theta), math.cos(theta)]])
    return np.matmul(rot_mat, point)


def rotate_frame(set, theta):
    out = []
    for i in set:
        out.append(rotate(i, theta))
    return out


def fitter(points_in, angle_mesh):
    out = []
    frame = FRAME_POINTS
    error = np.inf
    j = 0
    while (j * angle_mesh < 2 * math.pi):
        error = 0
        for i in points_in:
            error += nearest(i, frame)
        frame = rotate_frame(frame, angle_mesh)
        out.append(error)
        j += 1
    val, idx = min((val, idx) for (idx, val) in enumerate(out))
    return val, idx * angle_mesh


def fit_all(obj, angle_mesh=0.1):
    obj_out = {}
    for i in obj.keys():
        obj_out[i] = {}
        slopes, projections = plane_maker(obj[i])
        obj_out[i]['slopes'] = slopes
        obj_out[i]['projected-points'] = projections
        plane_points, affine_map = affine_trafo(slopes, projections)
        obj_out[i]['plane-points'] = plane_points
        error, angle = fitter(plane_points, angle_mesh)
        obj_out[i]['frame-points'] = rotate_frame(FRAME_POINTS, angle)
        sensor_points = rotate_frame(SENSOR_POINTS, angle)
        obj_out[i]['sensor-points-plane'] = sensor_points
        sensor_points = list(
            map(
                lambda x: np.matmul(affine_map, np.append(x, [SENSOR_Z, 1]))[
                    0:3], sensor_points))
        obj_out[i]['sensor-points-3d'] = sensor_points
    return obj_out

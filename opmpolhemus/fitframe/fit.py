import math
import numpy as np

from .plane import plane_maker
from .projection import affine_trafo

from constants import Constants

DELTA = Constants.PEN_POINT_SIZE
RIDGE = Constants.RIDGE_SIZE
XSIZE = Constants.HOLDER_XSIZE
YSIZE = Constants.HOLDER_YSIZE
YCELL = Constants.CELL_POS_Y
ZCELL = Constants.CELL_POS_Z

ANGLE_MESH = Constants.ANGLE_FIT_MESH

FRAME_POINTS = [(RIDGE + DELTA, YSIZE + DELTA), (XSIZE + DELTA, RIDGE + DELTA),
                (XSIZE + DELTA, -(RIDGE + DELTA)),
                (RIDGE + DELTA, -(YSIZE + DELTA)),
                (-(RIDGE + DELTA), -(YSIZE + DELTA)),
                (-(XSIZE + DELTA), -(RIDGE + DELTA)),
                (-(XSIZE + DELTA), (RIDGE + DELTA)),
                (-(RIDGE + DELTA), YSIZE + DELTA)]

SENSOR_POINTS = [(0.0, YCELL), (0.0, -YCELL)]


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
        slopes, projections, plane_fit_error = plane_maker(obj[i])
        plane_points, affine_map = affine_trafo(slopes, projections)
        frame_fit_error, angle = fitter(plane_points, angle_mesh)
        sensor_points_plane = rotate_frame(SENSOR_POINTS, angle)
        sensor_points_space = list(
            map(lambda x: np.matmul(affine_map, np.append(x, [ZCELL, 1]))[0:3],
                sensor_points_plane))
        sensor_points_frame_3d = list(
            map(lambda x: np.matmul(affine_map, np.append(x, [0, 1]))[0:3],
                sensor_points_plane))
        frame_center_of_mass = np.matmul(affine_map, np.array(
            (0, 0, 0, 1)))[0:3]
        obj_out[i]['sensor-points-3d'] = sensor_points_space
        obj_out[i]['frame-fit-error'] = frame_fit_error
        obj_out[i]['plane-fit-error'] = plane_fit_error
        obj_out[i]['sensor-points-frame-3d'] = sensor_points_frame_3d
        obj_out[i]['sensor-points-plane'] = sensor_points_plane
        obj_out[i]['slopes'] = slopes
        obj_out[i]['projected-points'] = projections
        obj_out[i]['plane-points'] = plane_points
        obj_out[i]['frame-points'] = rotate_frame(FRAME_POINTS, angle)
        obj_out[i]['com-base-frame'] = frame_center_of_mass
    return obj_out

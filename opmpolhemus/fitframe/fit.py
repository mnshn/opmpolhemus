import math
import numpy as np

DELTA = 0.001
RIDGE = 0.002
XSIZE = 0.0062
YSIZE = 0.0083

ERROR_MESH = 0.001

FRAME_POINTS = [(RIDGE + DELTA, YSIZE + DELTA), (XSIZE + DELTA, RIDGE + DELTA),
                (XSIZE + DELTA, -(RIDGE + DELTA)),
                (RIDGE + DELTA, -(YSIZE + DELTA)),
                (-(RIDGE + DELTA), -(YSIZE + DELTA)),
                (-(XSIZE + DELTA), -(RIDGE + DELTA)),
                (-(XSIZE + DELTA), (RIDGE + DELTA)),
                (-(RIDGE + DELTA), YSIZE + DELTA)]


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


def fitter(points_in, theta):
    out = []
    frame = FRAME_POINTS
    error = np.inf
    j = 0
    while (j * theta < 2 * math.pi):
        error = 0
        for i in points_in:
            error += nearest(i, frame)
        frame = rotate_frame(frame, theta)
        out.append(error)
        j += 1
    val, idx = min((val, idx) for (idx, val) in enumerate(out))
    return val, idx * theta

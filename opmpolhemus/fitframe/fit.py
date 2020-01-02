import math
import numpy as np


def distance_to_nearest(point, set):
    order = []
    set = np.array(set)
    for pt in set:
        order.append(np.linalg.norm(point - pt))
    return min(order)


def rotate(point, theta):
    rot_mat = np.array([[math.cos(theta), -math.sin(theta)],
                        [math.sin(theta), math.cos(theta)]])
    return np.matmul(rot_mat, point)


def rotate_frame(set, theta):
    out = []
    for point in set:
        out.append(rotate(point, theta))
    return out


def fitter(points_in, angle_mesh, frame):
    fit_errors = []
    error = np.inf
    phi = 0
    while (phi * angle_mesh < 2 * math.pi):
        error = 0
        for point in points_in:
            error += distance_to_nearest(point, frame)
        frame = rotate_frame(frame, angle_mesh)
        fit_errors.append(error)
        phi += 1
    min_val, min_index = min(
        (val, index) for (index, val) in enumerate(fit_errors))

    return min_index * angle_mesh, min_val

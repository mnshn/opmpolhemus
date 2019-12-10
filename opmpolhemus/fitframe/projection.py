import numpy as np
import scipy


def com(points):
    try:
        return (1 / len(points)) * np.sum(points, axis=0)
    except ZeroDivisionError:
        return np.inf


def affine_trafo(slopes, points):

    origin = com(points)
    a = slopes[0]
    b = slopes[1]
    c = slopes[2]
    point_on_plane = np.array([1 / a, -1 / b, c])
    vec = point_on_plane - origin
    vec = vec / np.linalg.norm(vec)
    normal = np.array([-a, -b, 1])
    normal = normal / np.linalg.norm(normal)
    V = np.cross(vec, normal)
    target = np.matrix.transpose(
        np.array([[0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]))
    affine = np.array([origin, origin + vec, origin + V, origin + normal])
    affine = np.vstack((np.matrix.transpose(affine), [1, 1, 1, 1]))
    affine_map = np.matmul(target, np.linalg.inv(affine))
    return list(
        map(lambda x: np.matmul(affine_map, np.hstack((x, 1)))[0:2], points))

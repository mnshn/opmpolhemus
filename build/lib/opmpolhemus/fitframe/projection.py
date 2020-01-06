import numpy as np
from opmpolhemus.helpers.com import com


def sign(flt):
    if flt < 0:
        return -1
    else:
        return 1


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
    normal_orientation = sign(np.dot(origin / np.linalg.norm(origin), normal))
    normal = normal_orientation * normal
    V = np.cross(vec, normal)
    target = np.matrix.transpose(
        np.array([[0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]))
    affine = np.array([origin, origin + vec, origin + V, origin + normal])
    affine = np.vstack((np.matrix.transpose(affine), [1, 1, 1, 1]))
    affine_map = np.matmul(target, np.linalg.inv(affine))

    return list(
        np.matmul(affine_map, np.hstack((point, 1)))[0:2]
        for point in points), np.linalg.inv(affine_map)

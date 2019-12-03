from sklearn.neighbors import KDTree
import numpy as np


def neighbors(pcloud, index, top=4, prev=0):
    tree = KDTree(pcloud, leaf_size=40)
    distances, indices = tree.query([pcloud[index]], k=top)
    isIndex = indices[0] != index
    isPrev = indices[0] != prev
    return indices[0][np.multiply(isIndex, isPrev)]


def query_sphere(pcloud, point, radius=0.01):
    tree = KDTree(pcloud, leaf_size=10)
    return tree.query_radius(point, r=radius)


def query_shell(pcloud, points, radius=0.01, delta=0.005):
    tree = KDTree(pcloud, leaf_size=10)
    pts_in = tree.query_radius(points, r=radius - delta)
    pts_out = tree.query_radius(points, r=radius + delta)
    return np.setdiff1d(pts_out[0], pts_in[0])

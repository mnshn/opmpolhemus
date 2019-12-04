from sklearn.neighbors import KDTree
import numpy as np


def neighbors(pcloud, index, history, top=5):
    tree = KDTree(pcloud, leaf_size=40)
    distances, indices = tree.query([pcloud[index]], k=top)
    history_mask = np.invert(np.isin(indices[0], np.array(list(history))))
    return indices[0][history_mask]


def query_sphere(pcloud, point, radius=0.01):
    tree = KDTree(pcloud, leaf_size=10)
    return tree.query_radius(point, r=radius)


def query_shell(pcloud, points, radius=0.01, delta=0.005):
    tree = KDTree(pcloud, leaf_size=10)
    pts_in = tree.query_radius(points, r=radius - delta)
    pts_out = tree.query_radius(points, r=radius + delta)
    return np.setdiff1d(pts_out[0], pts_in[0])


# def round_trip(index, i=0, history=set(), steps=3, pcl=opm_points):
#     print(i, index, history, neighbors(pcl, index, history))
#     while i < steps:
#         history.add(index)
#         for j in neighbors(pcl, index, history):
#             i += 1
#             round_trip(j, i, history)

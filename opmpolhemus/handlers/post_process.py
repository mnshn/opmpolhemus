import numpy as np
import copy


def com(points):
    try:
        return (1 / len(points)) * np.sum(points, axis=0)
    except ZeroDivisionError:
        return np.inf


def post_process(obj, pcl):
    opms_out = copy.deepcopy(obj)
    for i in opms_out.keys():
        for j in opms_out[i]:
            if len(opms_out[i][j]) > 1:
                coords = list(map(lambda x: pcl[x], opms_out[i][j]))
                opms_out[i][j] = com(coords)
            else:
                opms_out[i][j] = pcl[opms_out[i][j]][0]
    return opms_out

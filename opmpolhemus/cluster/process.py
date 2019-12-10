import numpy as np
import copy


def com(points):
    try:
        return (1 / len(points)) * np.sum(points, axis=0)
    except ZeroDivisionError:
        return np.inf


def post_process(obj, pcl):
    # opms_out = copy.deepcopy(obj)
    opms_out = {}
    for i in obj.keys():
        opms_out[i] = []
        for j in obj[i]:
            if len(obj[i][j]) > 1:
                coords = list(map(lambda x: pcl[x], obj[i][j]))
                opms_out[i].append(com(coords))
            else:
                opms_out[i].append(pcl[obj[i][j]][0])
    return opms_out

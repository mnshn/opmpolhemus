import numpy as np
from opmpolhemus.constants import Constants


def average_double_clicks(obj, pcl):
    opms_out = {}
    for i in obj.keys():
        opms_out[i] = []
        for j in obj[i]:
            if len(obj[i][j]) > 1:
                coords = list(pcl[x] for x in obj[i][j])
                opms_out[i].append(np.mean(coords, axis=0))
            else:
                opms_out[i].append(pcl[obj[i][j]][0])
    return opms_out


def remove_double_opms(obj):
    com_list = []
    for i in obj.keys():
        com_list.append(np.mean(obj[i], axis=0))
    for j in range(0, len(com_list)):
        for l in range(j + 1, len(com_list)):
            if np.linalg.norm(com_list[j] - com_list[l]
                              ) < Constants.OPM_DIFFERENCE_THRESHOLD:
                del obj[l]
    return obj


def post_process(obj, pcl):
    obj_out = average_double_clicks(obj, pcl)
    obj_out = remove_double_opms(obj_out)
    return np.array(list(obj_out.values()))

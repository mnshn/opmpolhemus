import time
import numpy as np
import copy

from constants import Constants

OPMS = Constants.TOTAL_OPMS


def com(points):
    try:
        return (1 / len(points)) * np.sum(points, axis=0)
    except ZeroDivisionError:
        return np.inf


def diff_of_com(points):
    try:
        avg = 0
        center_of_mass = com(points)
        for i in points:
            avg += np.linalg.norm(i - center_of_mass)
        return avg / len(points)
    except ZeroDivisionError:
        return np.inf


def is_not_part(p_index,
                K_index,
                points,
                pcl,
                com_threshold=Constants.COM_THRESHOLD,
                distance_threshold=Constants.DISTANCE_THRESHOLD):
    points = np.array(list(map(lambda x: pcl[x], points)))
    far_from_com = (p_index > 6) and abs(
        np.linalg.norm(com(points) - pcl[K_index]) -
        diff_of_com(points)) > com_threshold
    very_far_from_previous = (
        p_index > 0) and np.linalg.norm(pcl[K_index] -
                                        pcl[K_index - 1]) > distance_threshold
    return (far_from_com or very_far_from_previous)


def cluster_opms(pcl,
                 start=8,
                 double_click_threshold=Constants.DOUBLE_CLICK_THRESHOLD):
    output = {}
    K = start
    for i in range(0, OPMS):
        output[i] = {}
        point_index = 0
        j = 0
        while point_index < Constants.MAX_POINTS_PER_OPM:
            unique_points_so_far = list(
                map(lambda x: x[0], list(output[i].values())))
            if is_not_part(point_index, K, unique_points_so_far, pcl):
                print('📸 OPM {};'.format(i),
                      '{} corners out of {} points'.format(point_index, j),
                      'ind {} - {}'.format(K - j, K - 1))
                break
            else:
                for L in range(0, point_index):
                    if np.linalg.norm(pcl[K] - pcl[output[i][L][0]]
                                      ) < double_click_threshold:
                        output[i][L].append(K)
                        break
                else:
                    output[i][point_index] = [K]
                    point_index += 1
                j += 1
            K += 1
    return output

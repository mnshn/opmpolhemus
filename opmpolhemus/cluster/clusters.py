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


def is_not_part(unique_pen_click,
                pcl_index,
                points,
                pcl,
                com_threshold=Constants.COM_THRESHOLD,
                distance_threshold=Constants.DISTANCE_THRESHOLD):
    points = np.array(list(map(lambda x: pcl[x], points)))
    far_from_com = (unique_pen_click > 6) and abs(
        np.linalg.norm(com(points) - pcl[pcl_index]) -
        diff_of_com(points)) > com_threshold
    very_far_from_previous = (unique_pen_click > 0) and np.linalg.norm(
        pcl[pcl_index] - pcl[pcl_index - 1]) > distance_threshold
    return (far_from_com or very_far_from_previous)


def cluster_opms(pcl,
                 start=Constants.DEFAULT_START,
                 double_click_threshold=Constants.DOUBLE_CLICK_THRESHOLD):
    output = {}
    pcl_index = start
    i = -1
    while pcl_index < len(pcl):
        i += 1
        output[i] = {}
        unique_pen_click = 0
        pen_click = 0
        while pen_click < Constants.MAX_POINTS_PER_OPM and pcl_index < len(
                pcl):
            unique_points_so_far = list(
                map(lambda x: x[0], list(output[i].values())))
            if is_not_part(unique_pen_click, pcl_index, unique_points_so_far,
                           pcl):
                print(
                    '📸 OPM {};'.format(i),
                    '{} corners out of {} points'.format(
                        unique_pen_click, pen_click),
                    'ind {} - {}'.format(pcl_index - pen_click, pcl_index - 1))
                break
            else:
                for L in range(0, unique_pen_click):
                    if np.linalg.norm(pcl[pcl_index] - pcl[output[i][L][0]]
                                      ) < double_click_threshold:
                        output[i][L].append(pcl_index)
                        break
                else:
                    output[i][unique_pen_click] = [pcl_index]
                    unique_pen_click += 1
                pen_click += 1
            pcl_index += 1
    return output

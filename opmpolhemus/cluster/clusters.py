import numpy as np

from opmpolhemus.constants import Constants

from opmpolhemus.helpers.com import com
from opmpolhemus.helpers.com import diff_of_com


def next_opm(frame,
             unique_pen_click,
             pcl_index,
             points,
             turns,
             pcl,
             com_threshold=Constants.COM_THRESHOLD,
             distance_threshold=Constants.DISTANCE_THRESHOLD):
    points = list(pcl[i] for i in points)
    far_from_com = ((turns + 1) * unique_pen_click > frame.order - 1) and abs(
        np.linalg.norm(com(points) - pcl[pcl_index]) -
        diff_of_com(points)) > com_threshold

    very_far_from_previous = (unique_pen_click > 0) and np.linalg.norm(
        pcl[pcl_index] - pcl[pcl_index - 1]) > distance_threshold

    return (far_from_com or very_far_from_previous)


def cluster_opms(pcl,
                 frame,
                 double_click_threshold=Constants.DOUBLE_CLICK_THRESHOLD):
    output = {}
    pcl_index = 0
    opm_index = -1
    while pcl_index < len(pcl):
        opm_index += 1
        output[opm_index] = {}
        unique_pen_click = 0
        turns = 0
        while turns < frame.turns and pcl_index < len(pcl):
            unique_points_so_far = list(x[0]
                                        for x in output[opm_index].values())
            if next_opm(frame, unique_pen_click, pcl_index,
                        unique_points_so_far, turns, pcl):
                break
            else:
                for index, value in enumerate(unique_points_so_far):
                    if np.linalg.norm(pcl[pcl_index] -
                                      pcl[value]) < double_click_threshold:
                        output[opm_index][index].append(pcl_index)
                        if (not value == pcl_index - 1):
                            unique_pen_click += 1
                        break
                else:
                    output[opm_index][unique_pen_click] = [pcl_index]
                    unique_pen_click += 1
            pcl_index += 1
            if unique_pen_click == frame.order:
                turns += 1
    return output

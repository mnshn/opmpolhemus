import numpy as np

from opmpolhemus.constants import Constants

from opmpolhemus.helpers.com import com
from opmpolhemus.helpers.com import diff_of_com


def next_opm(frame,
             point,
             pcl_index,
             unique_points,
             turns,
             pcl,
             com_threshold=Constants.COM_THRESHOLD,
             distance_threshold=Constants.DISTANCE_THRESHOLD):
    unique_points = list(pcl[i] for i in unique_points)

    far_from_com = ((turns + 1) * point > frame.order - 1) and abs(
        np.linalg.norm(com(unique_points) - pcl[pcl_index]) -
        diff_of_com(unique_points)) > com_threshold

    very_far_from_previous = (
        point > 0) and np.linalg.norm(pcl[pcl_index] -
                                      pcl[pcl_index - 1]) > distance_threshold

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
        unique_point = 0
        turns = 0
        while turns < frame.turns and pcl_index < len(pcl):
            unique_points_so_far = list(x[0]
                                        for x in output[opm_index].values())
            if next_opm(frame, unique_point, pcl_index, unique_points_so_far,
                        turns, pcl):
                break
            else:
                for index, value in enumerate(unique_points_so_far):
                    if np.linalg.norm(pcl[pcl_index] -
                                      pcl[value]) < double_click_threshold:
                        output[opm_index][index].append(pcl_index)
                        if (not value == pcl_index - 1):
                            unique_point += 1
                        break
                else:
                    output[opm_index][unique_point] = [pcl_index]
                    unique_point += 1
            pcl_index += 1
            if unique_point == frame.order:
                turns += 1
    return output

import numpy as np
OPMS = 34


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


def is_not_part(p_index, K_index, points, pcl, com_threshold):
    return (
        (p_index > 6) and
        abs(np.linalg.norm(com(points) - pcl[K_index]) - diff_of_com(points)) >
        com_threshold)


def looper(pcl, start=8, double_click_threshold=10e-4):
    output = {}
    K = start
    for i in range(0, OPMS):
        output[i] = {}
        point_index = 0
        j = 0
        while point_index < 15:
            unique_points_so_far = list(
                map(lambda x: x[0], list(output[i].values())))
            if is_not_part(point_index, K, unique_points_so_far, pcl, 0.01):
                print(
                    '📸 OK, that was OPM {}'.format(i),
                    'Found {} corners with a total of {} points'.format(
                        point_index,
                        j), 'indices {} through {}'.format(K - j, K - 1))
                break
            else:
                for L in range(0, point_index):
                    if np.linalg.norm(
                            pcl[K] - output[i][L][0]) < double_click_threshold:
                        output[i][L].append(pcl[K])
                        break
                else:
                    output[i][point_index] = [pcl[K]]
                    point_index += 1
                j += 1
            K += 1
    return output

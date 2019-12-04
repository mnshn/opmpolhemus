import numpy as np
OPMS = 2


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
    ell = start
    for i in range(0, OPMS):
        output[i] = {}
        point_index = 0
        j = 0
        while point_index < 15:
            unique_points_so_far = list(
                map(lambda x: x[0], list(output[i].values())))
            # K = start + (i + 1) * j
            if is_not_part(point_index, ell, unique_points_so_far, pcl, 0.01):
                print(
                    ell,
                    abs(
                        np.linalg.norm(com(unique_points_so_far) - pcl[ell]) -
                        diff_of_com(unique_points_so_far)))

                break
            else:
                for L in range(0, point_index):
                    if np.linalg.norm(pcl[ell] - output[i][L][0]
                                      ) < double_click_threshold:
                        output[i][L].append(pcl[ell])
                        break
                else:
                    output[i][point_index] = [pcl[ell]]
                    point_index += 1
                j += 1
            ell += 1
            print(ell)
    print(output)
    return output

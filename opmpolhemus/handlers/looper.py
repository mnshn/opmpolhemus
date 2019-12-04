import numpy as np
OPMS = 1


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


def looper(pcl, start=8, double_click_threshold=10e-4):
    output = {}
    for i in range(0, OPMS):
        output[i] = {}
        point_index = 0
        j = 0
        while point_index < 9:
            points_so_far = list(map(lambda x: x[0], list(output[0].values())))
            K = start + (i + 1) * j
            print(
                np.linalg.norm(com(points_so_far) - pcl[K]) -
                diff_of_com(points_so_far))
            # print(
            #     'away from com:',
            #     np.linalg.norm(com(points_so_far) - pcl[K]) /
            #     np.linalg.norm(com(points_so_far)))
            # print('delta with last:', np.linalg.norm(pcl[K] - pcl[K - 1]))
            for L in range(0, point_index):
                if np.linalg.norm(pcl[K] -
                                  output[i][L][0]) < double_click_threshold:
                    output[i][L].append(pcl[K])
                    j += 1
                    break
            else:
                output[i][point_index] = [pcl[K]]
                j += 1
                point_index += 1
    return output

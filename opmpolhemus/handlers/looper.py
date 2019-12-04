import numpy as np
OPMS = 1


def com(points):
    return 1 / len(points) * np.sum(points, axis=0)


def looper(pcl, start=8, double_click_threshold=10e-4):
    output = {}
    for i in range(0, OPMS):
        output[i] = {}
        point_index = 0
        j = 0
        while point_index < 9:
            K = start + (i + 1) * j
            # print(np.linalg.norm(pcl[K] - pcl[K - 1]))
            for L in range(0, point_index):
                if np.linalg.norm(pcl[K] -
                                  output[i][L][0]) < double_click_threshold:
                    output[i][L].append(pcl[K])
                    print('jaaa', K, point_index - L)
                    j += 1
                    break
            else:
                output[i][point_index] = [pcl[K]]
                j += 1
                point_index += 1
    points_so_far = list(map(lambda x: x[0], list(output[0].values())))
    print(com(points_so_far))
    print(output)
    return output

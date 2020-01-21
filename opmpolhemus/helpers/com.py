import numpy as np


def diff_of_com(points):
    try:
        avg = 0
        center_of_mass = np.mean(points, axis=0)
        for i in points:
            avg += np.linalg.norm(i - center_of_mass)
        return avg / len(points)
    except ZeroDivisionError:
        return np.inf

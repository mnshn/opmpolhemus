import numpy as np
from scipy import optimize
import functools


def plane_maker(points_in):
    def plane(x, y, slopes):
        a = slopes[0]
        b = slopes[1]
        c = slopes[2]
        z = a * x + b * y + c
        return z

    def error(slopes, points):
        result = 0
        for (x, y, z) in points:
            plane_z = plane(x, y, slopes)
            diff = abs(plane_z - z)
            result += diff**2
        return result

    error_eval = functools.partial(error, points=points_in)
    slopes0 = [0, 0, 0]
    optimal_slopes = optimize.minimize(error_eval, slopes0)
    a = optimal_slopes.x[0]
    b = optimal_slopes.x[1]
    c = optimal_slopes.x[2]
    n = np.array([-a, -b, 1])
    nnorm = np.linalg.norm(n)
    n = n / nnorm
    projected_points = []
    for i in points_in:
        projected_points.append((i - (np.dot(i, n) - c / nnorm) * n))
    return [a, b, c], projected_points

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
    optimal_error = optimal_slopes.fun
    a = optimal_slopes.x[0]
    b = optimal_slopes.x[1]
    c = optimal_slopes.x[2]
    n = np.array([-a, -b, 1])
    nnorm = np.linalg.norm(n)
    n = n / nnorm
    projected_points = []
    Oz = np.array([0, 0, c])
    # Or the homogeneous way. Gives same result
    # T = np.array([[1, 0, 0, a], [0, 1, 0, b], [0, 0, 1, -1], [-a, -b, 1, 0]])
    # Tinv = np.linalg.inv(T)
    for i in points_in:
        # B = np.array([i[0], i[1], i[2], c])
        # projected_points.append(np.matmul(Tinv, B)[0:3])
        projected_points.append(i - (np.dot(i - Oz, n) * n))
    return [a, b, c], projected_points, optimal_error

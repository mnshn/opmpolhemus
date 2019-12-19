import numpy as np
from scipy import optimize
import functools
import random


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
    tries = 0
    maxTries = 15
    optimal_error = np.inf
    error_mesh = 10e-6
    error_mem = np.inf
    while (tries < maxTries and optimal_error > error_mesh):
        tries += 1
        slopes0 = [
            random.uniform(-5, 5),
            random.uniform(-5, 5),
            random.uniform(-5, 5)
        ]
        tries_slopes = optimize.minimize(error_eval, slopes0)
        optimal_error = tries_slopes.fun
        if (optimal_error < error_mem):
            error_mem = optimal_error
            optimal_slopes = tries_slopes
    a = optimal_slopes.x[0]
    b = optimal_slopes.x[1]
    c = optimal_slopes.x[2]
    n = np.array([-a, -b, 1])
    nnorm = np.linalg.norm(n)
    n = n / nnorm
    projected_points = []
    Oz = np.array([0, 0, c])
    for i in points_in:
        projected_points.append(i - (np.dot(i - Oz, n) * n))
    return [a, b, c], projected_points, optimal_error

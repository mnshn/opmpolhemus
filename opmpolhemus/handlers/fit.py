import numpy as np
from scipy import optimize
import functools


def plane_maker(points_in, pcl):
    points_in = list(map(lambda x: tuple(pcl[x]), points_in))

    def plane(x, y, slopes):
        alpha = slopes[0]
        beta = slopes[1]
        gamma = slopes[2]
        z = alpha + beta * x + gamma * y
        return z

    def error(slopes, points):
        result = 0
        for (x, y, z) in points:
            plane_z = plane(x, y, slopes)
            diff = abs(plane_z - z)
            result += diff**2
        return result

    fun = functools.partial(error, points=points_in)
    slopes0 = [0, 0, 0]
    optimal_slopes = optimize.minimize(fun, slopes0)

    a = optimal_slopes.x[0]
    b = optimal_slopes.x[1]
    c = optimal_slopes.x[2]
    return [a, b, c]

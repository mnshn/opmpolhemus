import numpy as np
from scipy import optimize
import functools
import random
from scipy import odr


# Orthogonal regression:
def odr_fit(points):
    def f(B, input):
        x, y = input
        x = np.array(x)
        y = np.array(y)
        return B[0] * x + B[1] * y + B[2]

    linear = odr.Model(f)
    data = odr.Data([points[:, 0], points[:, 1]], points[:, 2])
    odr_fit = odr.ODR(data, linear, beta0=[0, 0, 0])
    output = odr_fit.run()
    return output.beta, output.sum_square


# Linear regression:
def lin_reg_fit(points):
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
            diff = abs(plane_z - z)**2
            result += diff
        return result

    error_eval = functools.partial(error, points=points)
    tries = 0
    maxTries = 30
    optimal_error = np.inf
    error_mesh = 10e-6
    while (tries < maxTries and optimal_error > error_mesh):
        slopes0 = [
            random.uniform(-5 + 3 * tries, 5 + 3 * tries),
            random.uniform(-5 + 3 * tries, 5 + 3 * tries),
            random.uniform(-5 + 3 * tries, 5 + 3 * tries)
        ]
        tries += 1
        optimal_slopes = optimize.minimize(error_eval, slopes0)
        optimal_error = optimal_slopes.fun
    return optimal_slopes.x, optimal_error


def plane_maker(points):

    slopes, optimal_error = lin_reg_fit(points)
    a = slopes[0]
    b = slopes[1]
    c = slopes[2]

    n = np.array([-a, -b, 1])
    nnorm = np.linalg.norm(n)
    n = n / nnorm
    projected_points = []
    Oz = np.array([0, 0, c])
    for i in points:
        projected_points.append(i - (np.dot(i - Oz, n) * n))
    return [a, b, c], projected_points, optimal_error

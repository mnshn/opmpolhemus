import numpy as np
from scipy import odr


# Orthogonal regression:
def odr_fit(points):
    points = np.array(points)

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


def plane_maker(points):

    slopes, optimal_error = odr_fit(points)
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

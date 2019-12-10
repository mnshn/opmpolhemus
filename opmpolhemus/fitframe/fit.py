import numpy as np

DELTA = 0.001
RIDGE = 0.002
XSIZE = 0.0062
YSIZE = 0.0083

FRAME_POINTS = [(RIDGE + DELTA, YSIZE + DELTA), (XSIZE + DELTA, RIDGE + DELTA),
                (XSIZE + DELTA, -(RIDGE + DELTA)),
                (RIDGE + DELTA, -(YSIZE + DELTA)),
                (-(RIDGE + DELTA), -(YSIZE + DELTA)),
                (-(XSIZE + DELTA), -(RIDGE + DELTA)),
                (-(XSIZE + DELTA), (RIDGE + DELTA)),
                (-(RIDGE + DELTA), YSIZE + DELTA)]


def nearest(point, set):
    order = []
    set = np.array(set)
    for i in set:
        order.append(np.linalg.norm(point - i))
    return min(order)


def fitter(points_in):
    error = 0
    for i in points_in:
        error += nearest(i, FRAME_POINTS)
    print(error)

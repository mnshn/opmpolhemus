from utils.parser import mat_parser
from plot.points import plot_points
import matplotlib.pyplot as plt

test_file = '../db/point.txt'

opm_points = mat_parser(test_file)

plot_points(opm_points)

plt.show()

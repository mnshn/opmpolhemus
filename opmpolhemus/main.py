from utils.parser import mat_parser
from plot.points import plot_points
from handlers.kd_tree import neighbors, query_radius
import matplotlib.pyplot as plt

test_file = '../db/point.txt'

opm_points = mat_parser(test_file)

neighbors(opm_points)
print(query_radius(opm_points))

plot_points(opm_points)

plt.show()

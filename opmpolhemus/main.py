import matplotlib.pyplot as plt
from utils.parser import mat_parser

from handler.coreg import CoReg

test_file = '../db/proper02/point.txt'
data = mat_parser(test_file)

coreg = CoReg(data, 'top')
coreg.show_coreg()

plt.show()

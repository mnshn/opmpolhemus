import os
import numpy as np


def mat_parser(file):
    output = []
    if os.path.basename(file).split('.')[1] == 'txt':
        f = open(file, 'r')
        for line in f:
            line = line.split('\n')[0]
            line = list(map(lambda x: float(x), line.split('\t')))
            output.append(line)
    return output

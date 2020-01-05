import os
import numpy as np


def mat_parser(file):
    output = []
    if os.path.basename(file).split('.')[1] == 'txt':
        with open(file, 'r') as f:
            for line in f:
                line = line.split('\n')[0]
                line = list(float(x) for x in line.split('\t'))
                output.append(line)
    return np.array(output)

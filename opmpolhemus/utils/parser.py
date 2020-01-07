import os
import numpy as np
import mne


def mat_parser(file):
    output = []
    if os.path.basename(file).split('.')[1] == 'txt':
        with open(file, 'r') as f:
            for line in f:
                line = line.split('\n')[0]
                line = list(float(x) for x in line.split('\t'))
                output.append(line)
    elif os.path.basename(file).split('.')[1] == 'fif':
        try:
            with mne.io.read_raw_fif(file, allow_maxshield=True) as f:
                for i in range(0, len(f.info['dig'])):
                    if f.info['dig'][i]['kind'] == 4:
                        output.append(
                            np.array(
                                list(
                                    np.float64(x)
                                    for x in f.info['dig'][i]['r'])))
        except RuntimeWarning:
            pass

    return np.array(output)

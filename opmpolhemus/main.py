from utils.parser import mat_parser
from handler.coreg import CoReg

test_file = '../db/proper02/point.txt'


def coreg(data, frame_style, log_level=0):
    parsed_data = mat_parser(data)
    coreg_out = CoReg(parsed_data, frame_style)
    if log_level == 1:
        coreg_out.show_coreg()
    return coreg_out.sensors


print(coreg(test_file, 'top', log_level=0))

from opmpolhemus.utils.parser import mat_parser
from opmpolhemus.handler.coreg import CoReg


def coreg(data, frame_style, log_level=0):
    parsed_data = mat_parser(data)
    coreg_out = CoReg(parsed_data, frame_style)
    if log_level == 1:
        coreg_out.show_coreg()
    return coreg_out.sensors


if __name__ == '__main__':
    import sys
    file_in = sys.argv[1]
    coreg(file_in, 'top', log_level=1)

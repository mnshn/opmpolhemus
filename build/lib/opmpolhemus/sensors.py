from opmpolhemus.utils.parser import mat_parser
from opmpolhemus.handler.sensors import Sensors


def sensors(data, frame_style, log_level=0):
    parsed_data = mat_parser(data)
    sensors_out = Sensors(parsed_data, frame_style)
    if log_level == 1:
        sensors_out.show_coreg()
    return sensors_out.sensors


if __name__ == '__main__':
    import sys
    file_in = sys.argv[1]
    sensors(file_in, 'top', log_level=1)

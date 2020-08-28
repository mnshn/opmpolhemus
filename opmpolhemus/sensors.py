from opmpolhemus.structures.sensors import Sensors
from opmpolhemus.utils.parser import mat_parser


def sensors(data, frame_style, log_level=0):

    parsed_data = mat_parser(data)
    sensors_out = Sensors(parsed_data, frame_style)
    if log_level == 1:
        sensors_out.show_sensors()
    # normals_out = sensors_out.normals
    return sensors_out.sensors


if __name__ == '__main__':
    import sys
    file_in = sys.argv[1]
    sensors_out = sensors(file_in, 'top', log_level=1)
    if sys.argv[2]:
        file_out = sys.argv[2]
        sensors_out = [x.tolist() for x in sensors_out]
        with open(file_out, 'w') as writer:
            writer.write(str(sensors_out))

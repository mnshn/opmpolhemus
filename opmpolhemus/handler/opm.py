import numpy as np

from opmpolhemus.constants import Constants

from opmpolhemus.fitframe.plane import plane_maker
from opmpolhemus.fitframe.projection import affine_trafo
from opmpolhemus.fitframe.fit import fitter

from opmpolhemus.handler.frame import Frame

from opmpolhemus.plot.points import frame_plot, plot_points

from opmpolhemus.helpers.rot import rotate_frame


class OPM:
    def __init__(self, data, frame_style):
        frame = Frame(style=frame_style)
        self.data = data
        self.frame = frame
        self.label = None
        self.slopes, self.projections, self.fit_error = plane_maker(data)
        self.plane_points, self.affine_map = affine_trafo(
            self.slopes, self.projections)
        self.frame_fit_angle, self.frame_fit_error = fitter(
            self.plane_points, Constants.ANGLE_FIT_MESH, self.frame.frame)
        self.frame_fit = rotate_frame(self.frame.frame, self.frame_fit_angle)
        self.sensor_plane = rotate_frame([self.frame.sensor[0:2]],
                                         self.frame_fit_angle)
        self.sensor = np.matmul(
            self.affine_map,
            np.append(self.sensor_plane[0], [self.frame.sensor[2], 1]))[0:3]
        self.com = np.matmul(self.affine_map, np.array((0, 0, 0, 1)))[0:3]

    def show_frame_fit(self):
        frame_plot(self.plane_points,
                   frame_points=self.frame_fit,
                   additional_points=self.sensor_plane,
                   name_label=self.label)

    def show_plane_fit(self):
        plot_points(self.data,
                    surface_slopes=self.slopes,
                    projected_points=self.projections,
                    name_label=self.label,
                    additional_points=[self.sensor])

    def __repr__(self):
        return f'OPM with com at {self.com}'

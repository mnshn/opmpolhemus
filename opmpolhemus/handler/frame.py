from constants import Constants
import sys
sys.path.append("..")

DELTA = Constants.PEN_POINT_SIZE
RIDGE = Constants.RIDGE_SIZE
XSIZE = Constants.HOLDER_XSIZE
YSIZE = Constants.HOLDER_YSIZE
ZSIZE = Constants.HOLDER_ZSIZE
YCELL = Constants.CELL_POS_Y
ZCELL = Constants.CELL_POS_Z


class Frame():
    def __init__(self, style='base'):
        self.style = style
        if style == 'base':
            self.order = 8
            self.frame = [(RIDGE + DELTA, YSIZE + DELTA),
                          (XSIZE + DELTA, RIDGE + DELTA),
                          (XSIZE + DELTA, -(RIDGE + DELTA)),
                          (RIDGE + DELTA, -(YSIZE + DELTA)),
                          (-(RIDGE + DELTA), -(YSIZE + DELTA)),
                          (-(XSIZE + DELTA), -(RIDGE + DELTA)),
                          (-(XSIZE + DELTA), (RIDGE + DELTA)),
                          (-(RIDGE + DELTA), YSIZE + DELTA)]
            self.sensor = (0.0, YCELL, ZCELL - 0.0015)
        elif style == 'top':
            self.order = 4
            self.frame = [(-XSIZE, YSIZE), (XSIZE, YSIZE), (XSIZE, -YSIZE),
                          (-XSIZE, -YSIZE)]
            self.sensor = (0.0, YCELL, ZSIZE - ZCELL)

    def __repr__(self):
        return '{} frame of {} points'.format(self.style, self.order)

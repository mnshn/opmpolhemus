from opmpolhemus.constants import Constants

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
            self.turns = 1
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
            self.turns = 2
            self.frame = [(-XSIZE + DELTA, YSIZE - DELTA),
                          (XSIZE - DELTA, YSIZE - DELTA),
                          (XSIZE - DELTA, -YSIZE + DELTA),
                          (-XSIZE + DELTA, -YSIZE + DELTA)]
            self.sensor = (0.0, YCELL, -(ZSIZE - ZCELL))

    def __repr__(self):
        return f'{self.style} frame of {self.order} points'

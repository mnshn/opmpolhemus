DELTA = 0.002
RIDGE = 0.002
XSIZE = 0.0062
YSIZE = 0.0083

FRAME_POINTS = [(RIDGE + DELTA, YSIZE + DELTA), (XSIZE + DELTA, RIDGE + DELTA),
                (XSIZE + DELTA, -(RIDGE + DELTA)),
                (RIDGE + DELTA, -(YSIZE + DELTA)),
                (-(RIDGE + DELTA), -(YSIZE + DELTA)),
                (-(XSIZE + DELTA), -(RIDGE + DELTA)),
                (-(XSIZE + DELTA), (RIDGE + DELTA)),
                (-(RIDGE + DELTA), YSIZE + DELTA)]

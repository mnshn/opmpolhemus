# opmpolhemus

This package computes the three dimensional spatial location for the center of
the sensor cell for all OPMs whose positions are measured by a polhemus device.
This is a necessary step in solving the *forward problem*.

## Hardware

The OPM device is the 
*[QZFM Gen-2](https://quspin.com/products-qzfm/)* produced by QuSpin. The
dimesions that are listed
[here](http://quspin.com/wp-content/uploads/2016/08/Gen-2.jpg) enter the code in
[`constants.py`](https://github.com/paulmoonshine/opmpolhemus/blob/master/opmpolhemus/constants.py).

Currently, [this](https://quspin.com/experimental-meg-cap/) cap is used. To
locate the sensors, we tap 8 specific points on the base frame of the holders that are
on this cap. One such base frame looks like, schematically, like this: 
```
        <-------+  16.6 +------->

                 OxxxxxO
  ^     +---------xxxxx---------+
  |     |                       |
  +    O|                       |O
       xx                       xx
 12.4  xx                       xx
       xx                       xx
  +    O|                       |O
  |     |                       |
  v     +---------xxxxx---------+
                 OxxxxxO
```
*Base frame of OPM holder. Dimensions are in millimeters.*

In this diagram, the `x`'s mark the location of the holder arms that are to
encapsulate the OPM. These arms extend outward in direction normal to the screen.
The rectangle drawn by the `-` lines and the `+` on the cornerss is the base
frame that sits close to the scalp and is the resting frame of the OPM. Finally,
the eight `O` points are the reference points that we mark with the polhemus (we
use this device)[https://polhemus.com/scanning-digitizing/digitizing-products/].
With these measured points (`N = 8 x # of OPMS` in total) as input in the form of a
`[N,3]` array, the location of the sensor within the OPM is computed for every
OPM.

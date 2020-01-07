# opmpolhemus

This package computes the three dimensional spatial location for the center of
the sensor cell for all OPMs whose positions are measured by a polhemus device.
This is a necessary step in solving the *forward problem*.

## Test

test by running 

`python -m unittest test.test` 

from the root of this project
folder, or run it as a module: 

`python -m opmpolhemus.sensors test/test_files/test01_raw.fif`

## Usage

To use this in your project, install with

`python setup.py install`

Then import as:

`from opmpolhemus.sensors import sensors`

The package does require: `mne`, `numpy`, `scipy` and `matplotlib`. The `mne` is required to accept `fif` files.

The function `sensors` accepts two required arguments: `sensors(data,
frame_style)`. The data should for now be a text file containing your
measurements in matrix form. The frame_style should be either `top` or `base`
(see below for more info on that).


### Data

Both `.fif` files and `.txt` files are accepted as `data`. When input is a
`.txt`, it is assumed the input is a matrix of the HPI measurements, *but only
the actual opm HPI measurments*, so not including the fiducial points and the
indicator points (typically 4 and 3 respectively). For a `.fif` file, nothing
extra needs to be done as the parser will itself only select the actual HPI
measurements.

## Hardware

The OPM device is the 
*[QZFM Gen-2](https://quspin.com/products-qzfm/)* produced by QuSpin. The
dimensions that are listed
[here](http://quspin.com/wp-content/uploads/2016/08/Gen-2.jpg) enter the code in
[`constants.py`](https://github.com/paulmoonshine/opmpolhemus/blob/master/opmpolhemus/constants.py).

For digitizing the points from which we compute the cell's locations, we
use [this
device](https://polhemus.com/scanning-digitizing/digitizing-products/).

Currently, [this](https://quspin.com/experimental-meg-cap/) cap is used. To
digitize the location of the sensor, we tap specific points on or around the OPM. Currently, we accommodate two sets of
specific points to tap, from which this program then computes the location of
the sensor. Such a set of specific points will be called a *frame*, and the
frames we allow for are dubbed: *base* and *top*, and are defined as follows:

## frame: base
```
        <-------+  16.6 +------->

                 OxxxxxO
  ^     +---------xxxxx---------+
  |     |                       |
  +    O|                       |O
       xx                       xx
 12.4  xx         z=1.5         xx
       xx                       xx
  +    O|                       |O
  |     |                       |
  v     +---------xxxxx---------+
                 OxxxxxO
```
*frame=base. Dimensions are in millimeters.*

In this diagram, an `x` marks the location of the holder arms that are to
encapsulate the OPM 
([see here](https://quspin.com/wp-content/uploads/2019/05/Holder-with-base-280x300.png)).
These arms extend outward in direction normal to the screen.
The rectangle drawn by the `-` lines and the `+` on the corners is the base
frame that sits close to the scalp and is the resting frame of the OPM. Finally,
the eight `O` points are the reference points that we mark with the polhemus.
With these measured points (`N = 8 x # of OPMS` in total for frame=top) as input in the form of an
`[N,3]` array, the location of the sensor within the OPM is computed for every
OPM. Because of the thickness of the base frame, the reference points *O* sit
slightly higher (`1.5mm`) than the OPM bottom, as noted in the diagram.

## frame: top
```
        <-------+  16.6 +------->

                   xxxxx
   ^     +---------xxxxx---------+
   |     |O                     O|
   +     |                       |
        xx                       xx
  12.4  xx         z=24.0        xx
        xx                       xx
   +     |                       |
   |     |O                     O|
   v     +---------xxxxx---------+
                   xxxxx
```
*frame=top. Dimensions in millimeters.*

For this frame style, we mark only the four top corners of the OPM, at the top
face of the OPM at `z=24mm`. These are four points, obviously. As there is not
real firm fixed base the polhemus style can rest on for this method, we advise
to do this measurement twice, that is, to go clock-wise and perform a total of
`8` measurements, tapping every corner twice. The program will recognize this
and average over very nearby points (also for the case of accidental
double-clicks).

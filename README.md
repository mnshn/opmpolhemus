# opmpolhemus

This package computes the three dimensional spatial location for a the sensor
cell for all OPMs that are measured by a polhemus device. 

## Hardware
The OPM device is the 
*[QZFM Gen-2](https://quspin.com/products-qzfm/)* produced by QuSpin. The
dimesions that are lister
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


import math

#Tilt pot setpoints
kMaxDown = .795
kMaxUp = .205
kTopShot = .292
kTopShotAtBase = .281
kBottom = .765
kShootLevel = .646
kShootAtBase = .528
kShootRamp = .400

class Settings():
    """Robot mapping. Values that are changed often go here."""

    #Numbers to be changed through drive station
    num_precision_one = 0.80
    num_precision_two = 0.50
    num_scaling = 1.25
    num_macro_timeout = 15

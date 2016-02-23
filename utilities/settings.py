import math

class Settings():
    """Robot mapping. Values that are changed often go here."""

    #Values to be changed through drive station
    num_precision_one = 0.60
    num_precision_two = 0.50
    num_scaling = 1.25
    num_macro_timeout = 15

    #Tilt pot setpoints .158
    kMaxDown = 0.69 #derp, was .790
    #Works so far ^
    kMaxUp = kMaxDown - 0.570
    kTop = kMaxUp + 0.050
    kTopShot = kMaxDown - 0.498
    kTopShotAtBase = kMaxDown - 0.509
    kBottom = kMaxDown - 0.050
    kShootLevel = kMaxDown - 0.144
    #Test and modify ^
    kShootAtBase = kMaxDown - 0.316
    #Test and modify ^
    #2nd set of wheels is touching batter
    kShootRamp = kMaxDown - 0.464
    #Test and modify ^
    #Backed into tower
    kLongShot = kMaxDown - 0.158
    #Works so far ^
    #14 feet from tower

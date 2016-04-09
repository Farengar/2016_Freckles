import math

class Settings():
    """Robot mapping. Values that are changed often go here."""

    #Values to be changed through drive station
    num_precision_one = 0.60
    num_precision_two = 0.50
    num_scaling = 1.25
    num_macro_timeout = 15
    str_macro_name = "macro.csv"

    #Tilt pot setpoints .158
#    kMaxDown = 0.70 #derp, was .790
 #   kMaxUp = kMaxDown - 0.580
  #  kTop = kMaxUp + 0.050
#    kTopShot = kMaxDown - 0.498
 #   kTopShotAtBase = kMaxDown - 0.509
  #  kBottom = kMaxDown - 0.050
 #   kShootLevel = kMaxDown - 0.144
 #   kShootAtBase = kMaxDown - 0.316
    #2nd set of wheels is touching batter
  #  kShootRamp = kMaxDown - 0.464
    #Backed into tower
   # kLongShot = kMaxDown - 0.158
    #14 feet from tower

    #Encoder shenanigans
    kMaxDown = 3600
    kMaxUp = 1500
    kTop = 2000
    kTopShot = 2300
    kTopShotAtBase = 2500 
    kBottom = 3300
    kShootLevel = 3000
    kShootAtBase = 2900
    kShootRamp = 2800
    kLongShot = 2700

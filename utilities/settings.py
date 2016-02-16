import math

#Tilt pot setpoints
kDown = 0 #Full down
kUp = 1 #Full up
kTop = .9 #Recommended top
kBottom = .1 #Recommended bottom
kShoot = .5 #Level surface shooting
kRamp = .7 #Shooting on the ramp

class Settings():
    """Robot mapping. Values that are changed often go here."""

    #Numbers to be changed through drive station
    num_precision_one = 0.80
    num_precision_two = 0.50
    num_scaling = 1.25
    num_macro_timeout = 15

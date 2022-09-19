from .Button import Button
from .Speaker import Speaker
from .LightMatrix import LightMatrix
from .StatusLight import StatusLight
from .MotionSensor import MotionSensor


class PrimeHub:
    """ PrimeHub """

    """ The Left Button on the Hub. """
    left_button = Button()

    """ The Right Button on the Hub. """
    right_button = Button()

    """ The speaker inside the Hub. """
    speaker = Speaker()

    """ The speaker inside the Hub. """
    light_matrix = LightMatrix()

    """ The Brick Status Light on the Hub’s Center Button. """
    status_light = StatusLight()

    """ The Motion Sensor inside the Hub. """
    motion_sensor = MotionSensor()

    """ The Port that's labeled "A" on the Hub. """
    PORT_A = "A"

    """ The Port that's labeled "B" on the Hub. """
    PORT_B = "B"

    """ The Port that's labeled "C" on the Hub. """
    PORT_C = "C"

    """ The Port that's labeled "D" on the Hub. """
    PORT_D = "D"

    """ The Port that's labeled "E" on the Hub. """
    PORT_E = "E"

    """ The Port that's labeled "F" on the Hub. """
    PORT_F = "F"

    def __init__(self):
        """ Constructor for PrimeHub """
        print("PrimeHub::__init__")

from time import sleep
import random

from .constants import hub_ports


class ForceSensor:
    """Force Sensor

    Functions to interact with force sensors

    """

    observed_force = 0
    pressed = False

    def __init__(self, port: str):
        """ Constructor for ForceSensor

        Parameters
        ---------
        port : str
            The port the force sensor is attached to the hum

        Raises
        ------
        TypeError
            port is not a string
        ValueError
            port is not a valid value

        """
        if not isinstance(port, str):
            raise TypeError("port must be a str")

        if port not in hub_ports:
            raise ValueError("port must be in %r" % hub_ports)

        print("ForceSensor::__init__")

    def is_pressed(self) -> bool:
        """Tests whether the button on the sensor is pressed.

        Returns
        -------
        bool
            True is the button is pressed

        """

        print("ForceSensor::is_pressed")
        self.pressed = bool(random.getrandbits(1))
        return self.pressed

    def get_force_newton(self) -> float:
        """Retrieves the measured force, in newtons between 0 and 10

        Returns
        -------
        float
            The measured force, specified in newtons.

        """
        print("ForceSensor::get_force_newton")
        self.observed_force = random.uniform(0.0, 10.0)
        return self.observed_force

    def get_force_percentage(self) -> int:
        """Retrieves the measured force as a percentage of the maximum force.

        Returns
        -------
        int
            The measured force, given as a percentage.

        """
        print("ForceSensor::get_force_percentage")
        self.observed_force = random.randrange(0, 100)
        return self.observed_force

    def wait_until_pressed(self):
        """ Waits until the Force Sensor is pressed. """

        print("ForceSensor::wait_unit_pressed")
        sleep(random.randrange(1, 5))
        self.pressed = True

    def wait_until_released(self):
        """ Waits until the Force Sensor is released. """

        print("ForceSensor::wait_unit_released")
        sleep(random.randrange(1, 5))
        self.pressed = False

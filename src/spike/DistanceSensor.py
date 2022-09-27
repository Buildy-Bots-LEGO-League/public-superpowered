from time import sleep
import random

from .constants import hub_ports


class DistanceSensor:
    """DistanceSensor

    Functions to interact with distance sensors

    """

    lit_up = False

    observed_distance = 0

    def __init__(self, port: str):
        """ Constructor for DistanceSensor

        Parameters
        ----------
        port : str
            The port the distance sensor is attached to the hub

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

        print("DistanceSensor::__init__")

    def light_up_all(self, brightness: int = 100):
        """Lights up all the lights on the Distance Sensor at the specified brightness.

        Parameters
        ----------
        brightness : int
            The desired brightness of the lights on the Distance Sensor. 0 to 100% ("0" is off, and "100"
            is full brightness.)

        Raises
        ------
        TypeError
            brightness is not an integer.
        """

        print("DistanceSensor::light_up_all")
        self.light_up(brightness, brightness, brightness, brightness)
        self.lit_up = True

    def light_up(self, right_top: int = 100, left_top: int = 100, right_bottom: int = 100, left_bottom: int = 100):
        """Sets the brightness of the individual lights on the Color Sensor.

        This causes the Color Sensor to change modes, which can affect your program in unexpected ways.
        For example, the Color Sensor can't read colors when it's in light up mode.

        Parameters
        ----------
        right_top : int
            The brightness of the light that’s above the right part of the Distance Sensor.
            0 to 100% ("0" is off, and "100" is full brightness.)
        left_top : int
            The brightness of the light that’s above the left part of the Distance Sensor.
            0 to 100% ("0" is off, and "100" is full brightness.)
        right_bottom : int
            The brightness of the light that’s below the right part of the Distance Sensor.
            0 to 100% ("0" is off, and "100" is full brightness.)
        left_bottom : int
            The brightness of the light that’s below the left part of the Distance Sensor.
            0 to 100% ("0" is off, and "100" is full brightness.)

        Raises
        ------
        TypeError
            right_top, left_top, right_bottom, or left_bottom is not an integer.

        """

        if not isinstance(right_top, int):
            raise TypeError("light_up right_top must be an int")
        if not isinstance(left_top, int):
            raise TypeError("light_up left_top must be an int")
        if not isinstance(right_bottom, int):
            raise TypeError("light_up right_bottom must be an int")
        if not isinstance(left_bottom, int):
            raise TypeError("light_up left_bottom must be an int")

        if not 0 <= right_top <= 100:
            raise ValueError("light_up: light_1 out of range (0-100)")
        if not 0 <= left_top <= 100:
            raise ValueError("light_up: light_2 out of range (0-100)")
        if not 0 <= right_bottom <= 100:
            raise ValueError("light_up: right_bottom out of range (0-100)")
        if not 0 <= left_bottom <= 100:
            raise ValueError("light_up: left_bottom out of range (0-100)")

        print("DistanceSensor::light_up")
        print("Set right_top to %s" % right_top)
        print("Set left_top to %s" % left_top)
        print("Set right_bottom to %s" % right_bottom)
        print("Set right_bottom to %s" % left_bottom)
        self.lit_up = True

    def get_distance_cm(self, short_range: bool = False) -> float:
        """Retrieves the measured distance in centimeters.

        Parameters
        ----------
        short_range : bool
            Whether to use short range mode. Short range mode increases accuracy, but it can only
            detect nearby objects.

        Returns
        -------
        float
            The measured distance or None if the distance can't be measured.  Value will be between 0 and 200 cm.

        Raises
        ------
        TypeError
            short_range is not a boolean

        """

        if not isinstance(short_range, bool):
            raise TypeError("get_distance_cm short_range must be a boolean")

        print("DistanceSensor::get_distance_cm")
        self.observed_distance = random.uniform(0.0, 200.0)
        return self.observed_distance

    def get_distance_inches(self, short_range: bool = False) -> float:
        """Retrieves the measured distance in inches.

        Parameters
        ----------
        short_range : bool
            Whether to use short range mode. Short range mode increases accuracy, but it can only
            detect nearby objects.

        Returns
        -------
        float
            The measured distance or None if the distance can't be measured.  Value will be between 0 and 79 inches.

        Raises
        ------
        TypeError
            short_range is not a boolean

        """

        if not isinstance(short_range, bool):
            raise TypeError("get_distance_inches short_range must be a boolean")

        print("DistanceSensor::get_distance_inches")
        self.observed_distance = random.uniform(0.0, 79.0)
        return self.observed_distance

    def get_distance_percentage(self, short_range: bool = False) -> int:
        """Retrieves the measured distance as a percentage.

        Parameters
        ----------
        short_range : bool
            Whether to use short range mode. Short range mode increases accuracy, but it can only
            detect nearby objects.

        Returns
        -------
        int
            The measured distance or None if the distance can't be measured.  Value will be between 0 and 100%.

        Raises
        ------
        TypeError
            short_range is not a boolean

        """

        if not isinstance(short_range, bool):
            raise TypeError("get_distance_percentage short_range must be a boolean")

        print("DistanceSensor::get_distance_percentage")
        self.observed_distance = random.randint(0, 100)
        return self.observed_distance

    def wait_for_distance_farther_than(self, distance: float, unit: str = "cm", short_range: bool = False):
        """Waits until the measured distance is greater than the specified distance.

        Parameters
        ----------
        distance : float
            The target distance to be detected from the sensor to an object.

        unit : str
          The unit in which the distance is measured.  Allowed values cm, in, %

        short_range : bool
            Whether to use short range mode. Short range mode increases accuracy, but it can only
            detect nearby objects.

        Returns
        -------
        int
            The measured distance or None if the distance can't be measured.  Value will be between 0 and 100%.

        Raises
        ------
        TypeError
            distance is not a number, unit is not a string, or short_range is not a boolean.

        ValueError
            unit is not one of the allowed values.

        """

        if isinstance(distance, int):
            distance = distance * 1.0
        if not isinstance(distance, float):
            raise TypeError("wait_for_distance_farther_than distance must be a float")
        if not isinstance(unit, str):
            raise TypeError("wait_for_distance_farther_than unit must be a string")
        if not isinstance(short_range, bool):
            raise TypeError("wait_for_distance_farther_than short_range must be a boolean")

        if unit not in {"cm", "in", "%"}:
            raise ValueError("wait_for_distance_farther_than: unit must be one of 'cm', 'in', '%'")

        sleep(random.randint(1, 5))
        print("DistanceSensor::wait_for_distance_farther_than")
        self.observed_distance = distance

    def wait_for_distance_closer_than(self, distance: float, unit: str = "cm", short_range: bool = False):
        """Waits until the measured distance is less than the specified distance.

        Parameters
        ----------
        distance : float
            The target distance to be detected from the sensor to an object.

        unit : str
          The unit in which the distance is measured.  Allowed values cm, in, %

        short_range : bool
            Whether to use short range mode. Short range mode increases accuracy, but it can only
            detect nearby objects.

        Returns
        -------
        int
            The measured distance or None if the distance can't be measured.  Value will be between 0 and 100%.

        Raises
        ------
        TypeError
            distance is not a number, unit is not a string, or short_range is not a boolean.

        ValueError
            unit is not one of the allowed values.

        """

        if isinstance(distance, int):
            distance = distance * 1.0
        if not isinstance(distance, float):
            raise TypeError("wait_for_distance_closer_than distance must be a float")
        if not isinstance(unit, str):
            raise TypeError("wait_for_distance_closer_than unit must be a string")
        if not isinstance(short_range, bool):
            raise TypeError("wait_for_distance_closer_than short_range must be a boolean")

        if unit not in {"cm", "in", "%"}:
            raise ValueError("wait_for_distance_closer_than: unit must be one of 'cm', 'in', '%'")

        sleep(random.randint(1, 5))
        print("DistanceSensor::wait_for_distance_closer_than")
        self.observed_distance = distance

from time import sleep
import random
from .constants import hub_ports, valid_colors


class ColorSensor:
    """Color sensor

    Functions to interact with color sensors.

    """

    observed_color = None
    observed_ambient_light = 0
    observed_reflected_light = 0
    observed_red = 0
    observed_green = 0
    observed_blue = 0
    observed_overall_intensity = 0
    lights = (False, False, False)

    def __init__(self, port: str):
        """ Constructor for ColorSensor
        
        Parameters
        ----------
        port : str
            The port the color sensor is attached to the hub

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

        print("ColorSensor::__init__")

    def get_color(self) -> str:
        """Retrieves the detected color of a surface.

        Returns
        -------
        str
            The name of the detected color. black','violet','blue','cyan','green','yellow','red','white',None
        """

        print("ColorSensor::get_color")

        self.observed_color = random.choice(valid_colors)
        return self.observed_color

    def get_ambient_light(self) -> int:
        """ Retrieves the intensity of the ambient light.

        This causes the Color Sensor to change modes, which can affect your program in unexpected ways.
        For example, the Color Sensor can't read colors when it's in ambient light mode.

        Returns
        -------

        int
            The ambient light intensity between 0 and 100 inclusive.

        """

        print("ColorSensor::get_ambient_light")
        self.observed_ambient_light = random.randint(0, 100)
        return self.observed_ambient_light

    def get_reflected_light(self) -> int:
        """Retrieves the intensity of the reflected light.

        Returns
        -------

        int
            The reflected light intensity.

        """

        print("ColorSensor::get_reflected_light")
        self.observed_reflected_light = random.randint(0, 100)
        return self.observed_reflected_light

    def get_rbg_intensity(self) -> (int, int, int, int):
        """Retrieves the overall color intensity, and intensity of red, green, and blue.

        Returns
        -------
        tuple of int
            Red, green, blue, and overall intensity (0-1024)

        """

        print("ColorSensor::get_rbg_intensity")

        self.observed_red = random.randint(0, 1024)
        self.observed_green = random.randint(0, 1024)
        self.observed_blue = random.randint(0, 1024)
        self.observed_overall_intensity = random.randint(0, 1024)

        return self.observed_red, self.observed_green, self.observed_blue, self.observed_overall_intensity

    def get_red(self) -> int:
        """Retrieves the color intensity of red.

        Returns
        -------
        int
            Red intensity (0-100)

        """

        print("ColorSensor::get_red")
        self.observed_red = random.randint(0, 1024)
        return self.observed_red

    def get_green(self) -> int:
        """Retrieves the color intensity of green.

        Returns
        -------
        int
            Green intensity (0-100)

        """

        print("ColorSensor::get_green")
        self.observed_green = random.randint(0, 1024)
        return self.observed_green

    def get_blue(self) -> int:
        """Retrieves the color intensity of blue.

        Returns
        -------
        int
            Blue intensity (0-100)

        """
        print("ColorSensor::get_blue")
        self.observed_blue = random.randint(0, 1024)
        return self.observed_blue

    def wait_until_color(self, color: str):
        """Waits until the Color Sensor detects the specified color.

        Parameters
        ----------
        color : str
            The name of the color

        Raises
        ------
        TypeError
            The color is not a string or None.

        ValueError
            Color is not one of the allowed values

        """

        if color is not None and not isinstance(color, str):
            raise TypeError("wait_until_color color must be a str or None")

        if color not in valid_colors:
            raise ValueError("wait_until_color: color must be one of %r." % valid_colors)

        sleep(random.randint(1, 5))
        self.observed_color = color
        print("ColorSensor::wait_until_color")

    def wait_for_new_color(self) -> str:
        """Waits until the Color Sensor detects a new color.

        The first time this method is called, it immediately returns the detected color. After that,
        it waits until the Color Sensor detects a color that’s different from the color that was detected
        the last time this method was used.

        Returns
        -------

        str
            The name of the new color. ('black','violet','blue','cyan','green','yellow','red','white',None)

        """

        sleep(random.randint(1, 5))
        print("ColorSensor::wait_for_new_color")
        self.observed_color = random.choice(valid_colors)
        return self.observed_color

    def light_up_all(self, brightness: int = 100):
        """Lights up all the lights on the Color Sensor at the specified brightness.

        This causes the Color Sensor to change modes, which can affect your program in unexpected ways.
        For example, the Color Sensor can't read colors when it's in light up mode.

        Parameters
        ----------
        brightness : int
            The desired brightness of the lights on the Color Sensor. 0 to 100% ("0" is off, and "100"
            is full brightness.)

        Raises
        ------
        TypeError
            Brightness is not an integer.
        """

        print("ColorSensor::light_up_all")
        self.light_up(brightness, brightness, brightness)
        self.lights = (True, True, True)

    def light_up(self, light_1: int = 100, light_2: int = 100, light_3: int = 100):
        """Sets the brightness of the individual lights on the Color Sensor.

        This causes the Color Sensor to change modes, which can affect your program in unexpected ways.
        For example, the Color Sensor can't read colors when it's in light up mode.

        Parameters
        ----------
        light_1 : int
            The desired brightness of light 1.  0 to 100% ("0" is off, and "100" is full brightness.)
        light_2 : int
            The desired brightness of light 2.  0 to 100% ("0" is off, and "100" is full brightness.)
        light_3 : int
            The desired brightness of light 3.  0 to 100% ("0" is off, and "100" is full brightness.)

        Raises
        ------
        TypeError
            light_1, light_2, or light_3 is not an integer.

        """

        if not isinstance(light_1, int):
            raise TypeError("light_up light_1 must be an int")
        if not isinstance(light_2, int):
            raise TypeError("light_up light_2 must be an int")
        if not isinstance(light_3, int):
            raise TypeError("light_up light_3 must be an int")

        if not 0 <= light_1 <= 100:
            raise ValueError("light_up: light_1 out of range (0-100)")
        if not 0 <= light_2 <= 100:
            raise ValueError("light_up: light_2 out of range (0-100)")
        if not 0 <= light_3 <= 100:
            raise ValueError("light_up: light_3 out of range (0-100)")

        print("ColorSensor::light_up")
        print("Set light_1 to %s" % light_1)
        print("Set light_2 to %s" % light_2)
        print("Set light_3 to %s" % light_3)
        self.lights = (True, True, True)

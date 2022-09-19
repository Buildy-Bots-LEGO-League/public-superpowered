from .constants import valid_status_light_colors


class StatusLight:

    current_color = "white"
    illuminated = False

    def __init__(self):
        """ Constructor for StatusLight """
        print("StatusLight::__init__")

    def on(self, color: str = "white"):
        """ Sets the color of the light.

        Parameters
        ----------
        color : str
            Illuminates the Hub’s Brick Status Light in the specified color.

        Raises
        ------
        TypeError
            color is not a string.
        ValueError
            color is not one of the allowed values.

        """

        if not isinstance(color, str):
            raise TypeError("color must be a string")
        if color not in valid_status_light_colors:
            raise ValueError("color must be one of %r." % valid_status_light_colors)

        self.current_color = color
        self.illuminated = True

        print("StatusLight::on")

    def off(self):
        """ Turns off the light. """

        self.illuminated = False
        print("StatusLight::off")



from .constants import valid_lightmatrix_images


class LightMatrix:
    """ LightMatrix

    Following are all the functions that are linked to the Light Matrix.

    """

    current_image = ""

    def __init__(self):
        """ Constructor for LightMatrix """
        print("LightMatrix::__init__")

    def show_image(self, image: str, brightness: int = 100):
        """Shows an image on the Light Matrix.

        Parameters
        ----------
        image : str
            Name of the image
        brightness : int
            Brightness of the image. 0 to 100% ("0" is off, and "100" is full brightness.)

        Raises
        ------
        TypeError
            image is not a string or brightness is not an integer.
        ValueError
            image is not an allowed value or brightness is outside the range 0-100

        """

        if not isinstance(image, str):
            raise TypeError("show_image image must be a str")
        if not isinstance(brightness, int):
            raise TypeError("show_image brightness must be an int")

        if image not in valid_lightmatrix_images:
            raise ValueError("show_image: image must be one of %r." % valid_lightmatrix_images)

        if not 0 <= brightness <= 100:
            raise ValueError("show_image: brightness out of range (0-100)")

        self.current_image = image
        print("LightMatrix::show_image")
        print("Show %s at %s brightness" % (image, brightness))

    def set_pixel(self, x: int, y: int, brightness: int = 100):
        """Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.

        Parameters
        ----------
        x : int
            Pixel position, counting from the left.  In the range 0 to 4.
        y : int
            Pixel position, counting from the top. In the range 0 to 4
        brightness : int
            Brightness of the pixel. In the range 0 to 100.

        Raises
        ------
        TypeError
            One of the parameters is not an integer
        ValueError
            x or y is not in the range 0 to 4 or brightness is not in the range 0 to 100.

        """

        if not isinstance(x, int):
            raise TypeError("set_pixel x must be an int")
        if not isinstance(y, int):
            raise TypeError("set_pixel y must be an int")
        if not isinstance(brightness, int):
            raise TypeError("set_pixel brightness must be an int")

        if not 0 <= brightness <= 100:
            raise ValueError("set_pixel: brightness out of range (0-100)")
        if not 0 <= x <= 4:
            raise ValueError("set_pixel: x out of range (0-4)")
        if not 0 <= y <= 4:
            raise ValueError("set_pixel: y out of range (0-4)")

        self.current_image = ""
        print("LightMatrix::set_pixel")
        print("Set %s,%s to %s brightness", (x, y, brightness))

    def write(self, text):
        """ Displays text on the Light Matrix, one letter at a time, scrolling from right to left.

        Your program will not continue until all the letters have been shown.

        Parameters
        ----------
        text
            Text to write
        """

        self.current_image = ""
        print("LightMatrix::write")
        print("Display: %s" % str(text))

    def off(self):
        """Turn off all pixels on the light matrix"""

        self.current_image = ""
        print("LightMatrix::off")

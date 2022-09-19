from time import sleep
import random


class Button:
    """ Functions related to buttons """

    pressed = False

    def __init__(self):
        """ Constructor for Button """
        print("Button::__init__")

    def wait_until_pressed(self):
        """Wait unit the button is pressed."""
        print("Button::wait_until_pressed")
        sleep(random.randint(1, 5))
        self.pressed = False

    def wait_until_released(self):
        """Wait until the button is released."""
        print("Button::wait_until_released")
        sleep(random.randint(1, 5))
        self.pressed = False

    def was_pressed(self) -> bool:
        """Tests to see whether the button has been pressed since the last time this method called.
        Once this method returns "true," the button must be released and pressed again before it will
        return "true" again.

        Returns
        -------
        bool
            If the button was pressed.

        """

        print("Button::was_pressed")
        self.pressed = False
        return bool(random.getrandbits(1))

    def is_pressed(self):
        """Test whether the button is pressed.

        Returns
        -------
        bool
            True if the button is pressed, otherwise false

        """
        print("Button::was_pressed")
        self.pressed = False
        return bool(random.getrandbits(1))

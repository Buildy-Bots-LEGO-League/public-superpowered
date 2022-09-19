from .constants import valid_sound_names


class App:
    """Functions that are linked to the programmable elements of the SPIKE App."""

    current_volume = 100
    current_sound = None

    def __init__(self):
        """ Constructor for ColorSensor """
        print("App::__init__")

    def play_sound(self, name: str, volume: int = 100):
        """Plays a sound from the device (i.e., tablet or computer).
        The program will not continue until the sound has finished playing.
        If a sound with the specified name isn’t found, nothing will happen.

        Parameters
        ----------
        name : str
            The name of the sound to play.

        volume : int, optional {0-100}
            The volume at which the sound will be played.

        Raises
        ------
        TypeError
            The name is not a string or the volume is not an integer

        ValueError
            The name is not in the allowed list of sounds or the volume is outside the allowable range

        """

        if not isinstance(name, str):
            raise TypeError("play_sound name must be a str")
        if not isinstance(volume, int):
            raise TypeError("play_sound volume must be an int")

        if name not in valid_sound_names:
            raise ValueError("play_sound: name must be one of %r." % valid_sound_names)

        if not 0 <= volume <= 100:
            raise ValueError("play_sound: volume out of range (0-100)")

        self.current_sound = name
        self.current_volume = volume

        print("App::play_sound")
        print("Play %s at %s volume" % (name, volume))

    def start_sound(self, name: str, volume: int = 100):
        """Starts playing a sound from your device (i.e., tablet or computer).
        The program will not wait for the sound to finish playing before proceeding to the next command.
        If a sound with the specified name isn’t found, nothing will happen.

        Parameters
        ----------
        name : str
            The name of the sound to play.

        volume : int, optional {0-100}
            The volume at which the sound will be played.

        Raises
        ------
        TypeError
            The name is not a string or the volume is not an integer

        ValueError
            The name is not in the allowed list of sounds or the volume is outside the allowable range

        """

        if not isinstance(name, str):
            raise TypeError("start_sound name must be a str")
        if not isinstance(volume, int):
            raise TypeError("start_sound volume must be an int")

        if name not in valid_sound_names:
            raise ValueError("start_sound: name must be one of %r." % valid_sound_names)

        if not 0 <= volume <= 100:
            raise ValueError("start_sound: volume out of range (0-100)")

        self.current_sound = name
        self.current_volume = volume

        print("App::start_sound")
        print("Start %s at %s volume" % (name, volume))

from time import sleep


class Speaker:
    """ Speaker

    Following are all the functions that are linked to sounds coming out of the Hub.

    """

    current_volume = 100
    current_note = 0
    now_playing = False

    def __init__(self):
        """ Constructor for Speaker """
        print("Speaker::__init__")

    def beep(self, note: int = 60, seconds: float = 0.2):
        """ Plays a beep on the Hub.

        Your program will not continue until seconds have passed.

        Parameters
        ----------
            note : int
                The MIDI note number.
            seconds : float
                The duration of the beep, specified in seconds.

        Raises
        ------
        TypeError
            note is not an integer or seconds is not a number.
        ValueError
            note is not within the allowed range of 44-123.
        """

        if not isinstance(note, int):
            raise TypeError("note must be an integer")

        if 44 <= note <= 123:
            raise ValueError("note must be in the range 44 - 123 inclusive.")

        if not isinstance(seconds, float):
            raise TypeError("seconds must be a decimal number")

        self.current_note = note

        sleep(seconds)
        self.now_playing = False

        print("Speaker::beep")

    def start_beep(self, note: int = 60):
        """ Starts playing a beep.

        The beep will play indefinitely until stop() or another beep method is called.

        Parameters
        ----------
        note : int
            The MIDI note number.

        Raises
        ------
        TypeError
            note is not an integer.
        ValueError
            note is not within the allowed range of 44-123.

        """

        if not isinstance(note, int):
            raise TypeError("note must be an integer")

        if 44 <= note <= 123:
            raise ValueError("note must be in the range 44 - 123 inclusive.")

        self.now_playing = True
        self.current_note = note

        print("Speaker::start_beep")

    def stop(self):
        """ Stops any sound that is playing. """

        self.now_playing = False
        print("Speaker::stop")

    def get_volume(self) -> int:
        """ Retrieves the value of the speaker volume.

        This only retrieves the volume of the Hub, not the programming app.

        Returns
        -------
        int
            The current volume.

        """
        print("Speaker::get_volume")
        return self.current_volume

    def set_volume(self, volume: int = 100):
        """ Sets the speaker volume.

        If the assigned volume is out of range, the nearest volume (i.e., 0 or 100) will
        be used instead. This only sets the volume of the Hub, not the programming app.

        Parameters
        ----------
        volume : int
            The new volume percentage.

        Raises
        ------
        TypeError
            volume is not an integer

        """

        if not isinstance(volume, int):
            raise TypeError("volume must be an integer")

        if volume < 0:
            volume = 0
        elif volume > 100:
            volume = 100

        self.current_volume = volume

        print("Speaker::set_volume")

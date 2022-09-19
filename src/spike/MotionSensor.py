import random
from time import sleep

from .constants import valid_motionsensor_gestures, valid_motionsensor_orientations


class MotionSensor:
    """ MotionSensor

    Following are all the functions that are linked to the Hub’s Motion Sensor,
    which combines a three-axis accelerometer and a three-axis gyroscope.

    """

    observed_gesture = None
    observed_orientation = None
    roll = 0
    pitch = 0
    yaw = 0

    def __init__(self):
        """ Constructor for MotionSensor """
        print("MotionSensor::__init__")

    def was_gesture(self, gesture: str) -> bool:
        """ Tests whether a gesture has occurred since the last time was_gesture() was
        used, or since the beginning of the program (for the first use).

        Parameters
        ----------
        gesture : str
            The name of the gesture.

        Returns
        -------
        bool
            True if the gesture has occurred since the last time was_gesture() was called, otherwise false.

        Raises
        ------
        TypeError
            gesture is not a string.

        ValueError
            gesture is not a string.

        """

        if not isinstance(gesture, str):
            raise TypeError("gesture name must be a str")

        if gesture not in valid_motionsensor_gestures:
            raise ValueError("was_gesture: gesture must be one of %r." % valid_motionsensor_gestures)

        print("MotionSensor::was_gesture")
        self.observed_gesture = gesture
        return bool(random.getrandbits(1))

    def wait_for_new_gesture(self) -> str:
        """ Waits until a new gesture happens.

        Returns
        -------
        str
            The new gesture

        """

        print("MotionSensor::wait_for_new_gesture")
        sleep(random.randrange(1, 5))
        self.observed_gesture = random.choice(valid_motionsensor_gestures)
        return self.observed_gesture

    def wait_for_new_orientation(self) -> str:
        """ Waits until the Hub’s orientation changes.
        The first time this method is called, it will immediately return the current value.
        After that, calling this method will block the program until the Hub’s orientation
        has changed since the previous time this method was called.

        Returns
        -------
        str
            The Hub’s new orientation.
        """

        print("MotionSensor::wait_for_new_orientation")
        sleep(random.randrange(1, 5))
        self.observed_orientation = random.choice(valid_motionsensor_orientations)
        return self.observed_orientation

    def get_orientation(self) -> str:
        """ Retrieves the Hub's current orientation.

        Returns
        -------
        str
            The hub's orientation.
        """

        print("MotionSensor::get_orientation")
        self.observed_orientation = random.choice(valid_motionsensor_orientations)
        return self.observed_gesture

    def get_gesture(self) -> str:
        """ Retrieves the most recently-detected gesture.

        Returns
        -------
        str
            The gesture
        """

        print("MotionSensor::get_gesture")
        self.observed_gesture = random.choice(valid_motionsensor_gestures)
        return self.observed_gesture

    def get_roll_angle(self) -> int:
        """ Retrieves the Hub’s roll angle.
        Roll is the rotation around the front-back (longitudinal) axis. Yaw is the
        rotation around the front-back (vertical) axis. Pitch is the rotation around
        the left-right (transverse) axis.

        Returns
        -------
        int
            The roll angle, specified in degrees.
        """

        print("MotionSensor::get_roll_angle")
        self.roll = random.randrange(-180, 180)
        return self.roll

    def get_pitch_angle(self) -> int:
        """ Retrieves the Hub’s pitch angle.
        Pitch is the rotation around the left-right (transverse) axis. Roll is the rotation
        around the front-back (longitudinal) axis. Yaw is the rotation around the front-back
        (vertical) axis.

        Returns
        -------
        int
            The pitch angle, specified in degrees.
        """

        print("MotionSensor::get_pitch_angle")
        self.pitch = random.randrange(-180, 180)
        return self.pitch

    def get_yaw_angle(self) -> int:
        """ Retrieves the Hub’s yaw angle.
        Yaw is the rotation around the front-back (vertical) axis. Pitch the is rotation
        around the left-right (transverse) axis. Roll the is rotation around the front-back
        (longitudinal) axis.

        Returns
        -------
        int
            The yaw angle, specified in degrees.
        """

        print("MotionSensor::get_yaw_angle")
        self.yaw = random.randrange(-180, 180)
        return self.yaw

    def reset_yaw_angle(self):
        """ Sets the yaw angle to 0. """

        print("MotionSensor::reset_yaw_angle")
        self.yaw = 0

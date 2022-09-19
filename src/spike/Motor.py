from .constants import hub_ports, valid_motor_directions, valid_motor_stop_actions


class Motor:
    """ Motor
    Following are the functions that are linked to the Medium and Large Motors.
    """

    default_speed = 100

    current_speed = 0

    current_power = 100

    current_position = 0

    degrees_counter = 0

    stall_detection_enabled = True

    interrupted = False

    stalled = False

    stop_action = "coast"

    def __init__(self, port: str):
        """ Constructor for Motor

        Parameters
        ----------
        port : str
            The port which the motor is connected

        Raises
        ------
        TypeError
            port is not a str
        ValueError
            port is not a valid hub port
        """

        if not isinstance(port, str):
            raise TypeError("port must be a string")

        if port not in hub_ports:
            raise ValueError("port must be one of %r" % hub_ports)

        print("Motor::__init__")

    def run_to_position(self, degrees: int, direction: str = 'shortest path', speed: int = None):
        """ Runs the motor to an absolute position.
        
        The sign of the speed will be ignored (i.e., absolute value), and the motor will 
        always travel in the direction that’s been specified by the "direction" parameter. 
        If the speed is greater than 100, it will be limited to 100.
        
        Parameters
        ----------
        degrees : int
            The target position. (0-359)
            
        direction : str
            The direction to use to reach the target position.
            
        speed : int
            The motor’s speed as a percentage 0-100%
            
        Raises
        ------
        TypeError
            degrees or speed is not an integer or direction is not a string.
        ValueError
            direction is not one of the allowed values or degrees is not within the range 
            of 0-359 (both inclusive).
        
        """

        if not isinstance(degrees, int):
            raise TypeError("degrees must be a integer")

        if not 0 <= degrees <= 359:
            raise ValueError("run_to_position: degrees must be between 0 and 359 inclusive.")

        if not isinstance(direction, str):
            raise TypeError("direction must be a str")

        if direction not in valid_motor_directions:
            raise ValueError("run_to_position: direction must be one of %r." % valid_motor_directions)

        if speed is None:
            speed = self.get_default_speed()

        if not isinstance(speed, int):
            raise TypeError("speed must be a integer")

        if speed < 0:
            speed = speed * -1

        if speed > 100:
            speed = 100

        self.current_speed = speed
        self.current_speed = 0
        self.current_position = degrees

        print("Motor::run_to_position")

    def run_to_degrees_counted(self, degrees: int, speed: int = None):
        """ Runs the motor until the number of degrees counted is equal to the value that has
        been specified by the "degrees" parameter.

        The sign of the speed will be ignored, and the motor will always travel in the direction
        required to reach the specified number of degrees. If the speed is greater than "100,"
        it will be limited to "100."

        Parameters
        ----------
        degrees : int
            The target degrees counted.

        speed : int
            The motor’s speed as a percentage 0-100%

        Raises
        ------
        TypeError
            degrees or speed is not an integer.

        """

        if not isinstance(degrees, int):
            raise TypeError("degrees must be a integer")

        if speed is None:
            speed = self.get_default_speed()

        if not isinstance(speed, int):
            raise TypeError("speed must be a integer")

        if speed < 0:
            speed = speed * -1
        if speed > 100:
            speed = 100

        self.current_speed = speed
        self.current_speed = 0
        self.degrees_counter = degrees

        print("Motor::run_to_degrees_counted")

    def run_for_degrees(self, degrees: int, speed: int = None):
        """ Runs the motor for a specified number of degrees.

        Parameters
        ---------
        degrees : int
            The number of degrees that the motor should run.

        speed : int
            The motor’s speed.

        Raises
        ------
        TypeError
            degrees or speed is not an integer.
        """

        if not isinstance(degrees, int):
            raise TypeError("degrees must be a integer")

        if speed is None:
            speed = self.get_default_speed()

        if not isinstance(speed, int):
            raise TypeError("speed must be a integer")

        if speed < -100:
            speed = -100
        elif speed > 100:
            speed = 100

        self.current_speed = speed
        self.current_speed = 0
        self.degrees_counter = self.degrees_counter + degrees
        print("Motor::run_for_degrees")

    def run_for_rotations(self, rotations: float, speed: int = None):
        """Runs the motor for a specified number of rotations.

        Parameters
        ----------
        rotations : float
            The number of rotations that the motor should run.
        speed : int
            The motor’s speed.

        Raises
        ------
        TypeError
            rotations is not a number or speed is not an integer.

        """

        if not isinstance(rotations, float):
            raise TypeError("rotations must be a float")

        if speed is None:
            speed = self.get_default_speed()

        if not isinstance(speed, int):
            raise TypeError("speed must be an integer")

        if speed < -100:
            speed = -100
        elif speed > 100:
            speed = 100

        self.current_speed = speed
        self.current_speed = 0

        print("Motor::run_for_rotations")

    def run_for_seconds(self, seconds: float, speed: int = None):
        """ Runs the motor for a specified number of seconds.

        Parameters
        ----------
        seconds : float
            The number of seconds that the motor should run.
        speed : int
            The motor’s speed.

        Raises
        ------
        TypeError
            seconds is not a number or speed is not an integer.

        """

        if not isinstance(seconds, float):
            raise TypeError("seconds must be a float")

        if speed is None:
            speed = self.get_default_speed()

        if not isinstance(speed, int):
            raise TypeError("speed must be an integer")

        if speed < -100:
            speed = -100
        elif speed > 100:
            speed = 100

        self.current_speed = speed
        self.current_speed = 0

        print("Motor::run_for_seconds")

    def start(self, speed: int = None):
        """ Starts running the motor at a specified speed.

        The motor will keep moving at this speed until you give it another motor
        command or when your program ends.

        Parameters
        ----------
        speed : int
            The motor’s speed.

        Raises
        ------
        TypeError
            speed is not an integer.

        """

        if speed is None:
            speed = self.get_default_speed()

        if not isinstance(speed, int):
            raise TypeError("speed must be an integer")

        if speed < -100:
            speed = -100
        elif speed > 100:
            speed = 100

        self.current_speed = speed
        print("Motor::start")

    def stop(self):
        """ Stops the motor.
        What the motor does after it stops depends on the action that’s been set
        in set_stop_action(). The default value of set_stop_action() is "coast."

        """

        self.current_speed = 0
        print("Motor::stop")

    def start_at_power(self, power: int):
        """ Starts rotating the motor at a specified power level.

        The motor will keep moving at this power level until you give it another
        motor command or when your program ends.

        Parameters
        ----------
        power : int
            The power of the motor

        Raises
        ------
        TypeError
            power is not a number

        """

        if not isinstance(power, int):
            raise TypeError("power must be an integer")

        if power < -100:
            power = -100
        elif power > 100:
            power = 100

        self.current_power = power
        self.current_speed = self.get_default_speed()

        print("Motor::start_at_power")

    def get_speed(self) -> int:
        """ Retrieves the motor speed.

        Returns
        -------
        int
            The motor's current speed
        """
        print("Motor::get_speed")
        return self.current_speed

    def get_position(self) -> int:
        """ Retrieves the motor position. This is the clockwise angle between the moving
        marker and the zero-point marker on the motor.

        Returns
        -------
        int
            The motor’s position.

        """
        print("Motor::get_position")
        return self.current_position

    def get_degrees_counted(self) -> int:
        """ Retrieves the number of degrees that have been counted by the motor.

        Returns
        -------
        int
            The number of degrees that’s been counted.

        """
        print("Motor::get_degrees_counted")
        return self.degrees_counter

    def get_default_speed(self) -> int:
        """ Retrieves the current default motor speed.

        Returns
        -------
        int
            The default motor’s speed.

        """
        print("Motor::get_default_speed")
        return self.default_speed

    def was_interrupted(self) -> bool:
        """ Tests whether the motor was interrupted.

        Returns
        -------
        bool
            True if the motor was interrupted since the last time was_interrupted()
            was called, otherwise false.

        """
        print("Motor::was_interrupted")

        return_value = self.interrupted
        self.interrupted = False
        return return_value

    def was_stalled(self) -> bool:
        """ Tests whether the motor was stalled.

        Returns
        -------
        bool
            True if the motor has stalled since the last time was_stalled() was called,
            otherwise false.

        """
        print("Motor::was_stalled")
        return_value = self.stalled
        self.stalled = False
        return return_value

    def set_degrees_counted(self, degrees_counted: int):
        """ Sets the "number of degrees counted" to the desired value.

        Parameters
        ----------
        degrees_counted : int
            The value to which the number of degrees counted should be set.

        Raises
        ------
        TypeError
            degrees_counted is not an integer
        """

        if not isinstance(degrees_counted, int):
            raise TypeError("degrees_counted must be an integer")

        self.degrees_counter = degrees_counted

        print("Motor::set_degrees_counted")

    def set_default_speed(self, speed: int):
        """ Sets the default motor speed. This speed will be used when you omit the
        speed argument in one of the other methods, such as run_for_degrees.

        Setting the default speed does not affect any motors that are currently running.

        It will only have an effect when another motor method is called after this method.

        If the value of default_speed is outside the allowed range, the default speed
        will be set to "-100" or "100" depending on whether the value is negative or positive."""

        if not isinstance(speed, int):
            raise TypeError("speed must be an integer")

        if speed < -100:
            speed = -100
        elif speed > 100:
            speed = 100

        self.default_speed = speed

        print("Motor::set_default_speed")

    def set_stop_action(self, action: str = "coast"):
        """ Sets the default behavior when a motor stops.

        Parameters
        ----------
        action : str
            The desired motor behavior when the motor stops.

        Raises
        ------
        TypeError
            action is not a string.
        ValueError
            action is not one of the allowed values.

        """

        if not isinstance(action, str):
            raise TypeError("action must be a string")

        if action not in valid_motor_stop_actions:
            raise ValueError("set_stop_action: action must be one of %r." % valid_motor_stop_actions)

        print("Motor::set_stop_action")

        self.stop_action = action

    def set_stall_detection(self, stop_when_stalled: bool = True):
        """ Turns stall detection on or off.

        Stall detection senses when a motor has been blocked and can’t move. If stall detection
        has been enabled and a motor is blocked, the motor will be powered off after two seconds
        and the current motor command will be interrupted. If stall detection has been disabled,
        the motor will keep trying to run and programs will "get stuck" until the motor is no
        longer blocked.

        Stall detection is enabled by default.

        Parameters
        ----------
        stop_when_stalled : bool
            Choose "true" to enable stall detection or "false" to disable it.

        Raises
        ------
        TypeError
            stop_when_stalled is not a boolean.

        """

        self.stall_detection_enabled = stop_when_stalled
        print("Motor::set_stall_detection")

from .constants import valid_motor_units, valid_motor_stop_actions, valid_motor_rotation_unit_settings, hub_ports


class MotorPair:
    """ MotorPair

    MotorPair objects are used to control 2 motors simultaneously in opposite directions.
    To be able to use MotorPair, you must initialize both motors. """

    default_speed = 100

    stop_action = "coast"

    running = False

    motor_rotation = {17.6, "cm"}

    def __init__(self, left: str, right: str):
        """ Constructor for MotorPair

        Parameters
        ----------
        left : str
            The port of the left side motor
        right : str
            The port of the right side motor

        Raises
        ------
        TypeError
            left or right is not a str
        ValueError
            left or right is not a valid port
        """

        if not isinstance(left, str):
            raise TypeError("left must be a str")

        if not isinstance(right, str):
            raise TypeError("right must be a str")

        if left not in hub_ports:
            raise ValueError("left must be in %r" % hub_ports)

        if right not in hub_ports:
            raise ValueError("right must be in %r" % hub_ports)

        print("MotorPair::__init__")

    def move(self, amount: float, unit: str = 'cm', steering: int = 0, speed: int = None):
        """ Start both motors simultaneously to move a Driving Base.

        Steering = "0" makes the Driving Base go straight. Negative numbers make the Driving
        Base turn left. Positive numbers make the Driving Base turn right.

        The program will not continue until the specified value is reached.

        If the value of steering is equal to "-100" or "100," the Driving Base will perform a
        rotation on itself (i.e., "tank move") at the default speed of each motor.

        If the value of steering is outside the allowed range, the value will be set to
        "-100" or "100," depending on whether the value is positive or negative.

        If speed is outside the allowed range, the value will be set to "-100" or "100,"
        depending on whether the value is positive or negative.

        If the speed is negative, the Driving Base will move backward instead of forward.
        Likewise, if the "amount" is negative, the Driving Base will move backward instead of
        forward. If both the speed and the "amount" are negative, the Driving Base will move forward.

        When the specified unit is "cm" or "in," the "amount" of the unit parameter is equal to
        the horizontal distance that the Driving Base will travel before stopping. The relationship
        between the motor rotations and distance traveled can be adjusted by calling set_motor_rotation().

        When the "unit" is "rotations" or "degrees," the "amount" parameter value specifies how much
        the motor axle will turn before stopping.

        When the "unit" is "seconds," the "amount" parameter value specifies the duration that the
        motors will run before stopping.

        Parameters
        ----------
        amount : float
            The quantity to move in relation to the specified unit of measurement.
        unit : str
            The unit of measurement specified for the "amount" parameter.
        steering : int
            The direction and quantity to steer the Driving Base.
        speed : int
            The motor speed.

        Raises
        ------
        TypeError
            amount is not a number, or steering or speed is not an integer, or unit is not a string.
        ValueError
            unit is not one of the allowed values or steering or speed is outside the allowed range
        """

        if not isinstance(amount, float):
            raise TypeError("amount must be a float")

        if not isinstance(unit, str):
            raise TypeError("unit must be a str")

        if unit not in valid_motor_units:
            raise ValueError("move: unit must be one of %r." % valid_motor_units)

        if not isinstance(steering, int):
            raise TypeError("steering name must be a int")

        if not -100 <= steering <= 100:
            raise ValueError("move: steering must be between -100 and 100 inclusive.")

        if speed is None:
            speed = self.default_speed

        if not isinstance(speed, int):
            raise TypeError("speed must be a integer")

        if not -100 <= speed <= 100:
            raise ValueError("move: speed must be between -100 and 100 inclusive.")

        print("MotorPair::move")

    def start(self, steering: int = 0, speed: int = None):
        """ Start both motors simultaneously to move a Driving Base.

        Steering = "0" makes the Driving Base go straight. Negative numbers make the Driving Base
        turn left. Positive numbers make the Driving Base turn right.

        The program flow is not interrupted. This is most likely interrupted by sensor input and
        a condition.

        If the value of steering is equal to "-100" or "100," the Driving Base will perform a
        rotation on itself (i.e., "tank move") at the default speed of each motor.

        If the value of "steering" is outside the allowed range, the value will be set to
        "-100" or "100," depending on whether the value is positive or negative.

        If speed is outside the allowed range, the value will be set to "-100" or "100," depending
        on whether the value is positive or negative.

        If the speed is negative, the Driving Base will move backward instead of forward. Likewise,
        if the "amount" is negative, the Driving Base will move backward instead of forward. If both
        the speed and the "amount" are negative, the Driving Base will move forward.

        Parameters
        ----------
        steering : int
            The direction and quantity to steer the Driving Base.
        speed : int
            The motor speed.

        Raises
        ------
        TypeError
            steering or speed is not an integer.
        ValueError
            steering or speed is outside the allowed range
        """

        if not isinstance(steering, int):
            raise TypeError("steering must be a int")

        if not -100 <= steering <= 100:
            raise ValueError("start: steering must be between -100 and 100 inclusive.")

        if speed is None:
            speed = self.default_speed

        if not isinstance(speed, int):
            raise TypeError("speed must be a integer")

        if not -100 <= speed <= 100:
            raise ValueError("start: speed must be between -100 and 100 inclusive.")

        self.running = True

        print("MotorPair::start")

    def stop(self):
        """ Stops both motors simultaneously, which will stop a Driving Base.

        The motors will either actively hold their current position or coast freely depending
        on the option that’s been selected by set_stop_action().

        """

        self.running = False

        print("MotorPair::stop")

    def move_tank(self, amount: float, unit: str = 'cm', left_speed: int = None, right_speed: int = None):
        """ Moves the Driving Base using differential (tank) steering.

        The speed of each motor can be controlled independently for differential (tank) drive
        Driving Bases.

        When the specified unit is "cm" or "in," the "amount" of the unit parameter is equal
        to the horizontal distance that the Driving Base will travel before stopping. The
        relationship between the motor rotations and distance traveled can be adjusted by calling
        set_motor_rotation().

        When the "unit" is "rotations" or "degrees," the "amount" parameter value specifies how
        much the motor axle will turn before stopping.

        When the "unit" is "seconds," the "amount" parameter value specifies the duration that
        the motors will run before stopping.

        If left_speed or right_speed is outside the allowed range, the value will be set to
        "-100" or "100" depending on whether the value is positive or negative.

        If one of the speeds (i.e., left_speed or right_speed) is negative, the negative-speed
        motor will run backward instead of forward. If the "amount" parameter value is negative,
        both motors will rotate backward instead of forward. If both of the speed values
        (i.e., left_speed and right_speed) are negative and the "amount" parameter value is negative,
        both motors will rotate forward.

        The program will not continue until the specified value is reached.

        Parameters
        ----------
        amount : float
            The quantity to move in relation to the specified unit of measurement.
        unit : str
            The unit of measurement specified for the "amount" parameter.
        left_speed : int
            The speed of the left motor.
        right_speed : int
            The speed of the right motor.

        Raises
        ------
        TypeError
            amount, left_speed or right_speed is not a number or unit is not a string.
        ValueError
            unit is not one of the allowed values.

        """

        if not isinstance(amount, float):
            raise TypeError("amount must be a float")

        if not isinstance(unit, str):
            raise TypeError("unit must be a str")

        if unit not in valid_motor_units:
            raise ValueError("move_tank: unit must be one of %r." % valid_motor_units)

        if left_speed is None:
            left_speed = self.default_speed

        if not isinstance(left_speed, int):
            raise TypeError("left_speed must be a integer")

        if not -100 <= left_speed <= 100:
            raise ValueError("move_tank: left_speed must be between -100 and 100 inclusive.")

        if right_speed is None:
            right_speed = self.default_speed

        if not isinstance(right_speed, int):
            raise TypeError("right_speed must be a integer")

        if not -100 <= right_speed <= 100:
            raise ValueError("move_tank: right_speed must be between -100 and 100 inclusive.")

        print("MotorPair::move_tank")

    def start_tank(self, left_speed: int = None, right_speed: int = None):
        """ Starts moving the Driving Base using differential (tank) steering.

        The speed of each motor can be controlled independently for differential (tank)
        drive Driving Bases.

        If left_speed or right_speed is outside the allowed range, the value will be
        set to "-100" or "100" depending on whether the value is positive or negative.

        If the speed is negative, the motors will move backward instead of forward.

        The program flow is not interrupted. This is most likely interrupted by sensor
        input and a condition.

        Parameters
        ----------
        left_speed : int
            The speed of the left motor.
        right_speed : int
            The speed of the right motor.

        Raises
        ------
        TypeError
            left_speed or right_speed is not a number.
        ValueError
            left_speed or right_speed is outside the acceptable range.

        """
        if left_speed is None:
            left_speed = self.default_speed

        if not isinstance(left_speed, int):
            raise TypeError("left_speed must be a integer")

        if not -100 <= left_speed <= 100:
            raise ValueError("start_tank: left_speed must be between -100 and 100 inclusive.")

        if right_speed is None:
            right_speed = self.default_speed

        if not isinstance(right_speed, int):
            raise TypeError("right_speed must be a integer")

        if not -100 <= right_speed <= 100:
            raise ValueError("start_tank: right_speed must be between -100 and 100 inclusive.")

        print("MotorPair::start_tank")

    def start_at_power(self, power: int = 100, steering: int = 0):
        """ Starts moving the Driving Base without speed control.

        The motors can also be driven without speed control. This is useful when using your own
        control algorithm (e.g., a proportional line-follower).

        If the steering is outside the allowed range, the value will be set to "-100" or "100"
        depending on whether the value is positive or negative.

        If the power is outside the allowed range, the value will be set to "-100" or "100"
        depending on whether the value is positive or negative.

        If the power is negative, the Driving Base will move backward instead of forward.

        The program flow is not interrupted. This can most likely be interrupted by sensor input
        and a condition.

        Parameters
        ----------
        power : int
            The amount of power to send to the motors.
        steering : int
            The steering direction (-100 to 100). "0" makes the Driving Base move straight. Negative
            numbers make the Driving Base turn left. Positive numbers make the Driving Base turn right.

        Raises
        ------
        TypeError
            power or steering is not a number.
        ValueError
            power or steering is outside the acceptable range.
        """

        if not isinstance(power, int):
            raise TypeError("power must be a integer")

        if not -100 <= power <= 100:
            raise ValueError("start_at_power: power must be between -100 and 100 inclusive.")

        if not isinstance(steering, int):
            raise TypeError("steering must be a integer")

        if not -100 <= steering <= 100:
            raise ValueError("start_at_power: steering must be between -100 and 100 inclusive.")

        self.running = True

        print("MotorPair::start_at_power")

    def start_tank_at_power(self, left_speed: int = None, right_speed: int = None):
        """ Starts moving the Driving Base using differential (tank) steering without speed control.

        The motors can also be driven without speed control. This is useful when using your own
        control algorithm (e.g., a proportional line-follower).

        If the left_power or right_power is outside the allowed range, the value will be rounded
        to "-100" or "100" depending on whether the value is positive or negative.

        If the power is a negative value, the corresponding motor will move backward instead of forward.

        The program flow is not interrupted. This can most likely be interrupted by sensor input and a condition.

        Parameters
        ----------
        left_speed : int
            The speed of the left motor.
        right_speed : int
            The speed of the right motor.

        Raises
        ------
        TypeError
            left_speed or right_speed is not a number.
        ValueError
            left_speed or right_speed is outside the acceptable range.

        """
        if left_speed is None:
            left_speed = self.default_speed

        if not isinstance(left_speed, int):
            raise TypeError("left_speed must be a integer")

        if not -100 <= left_speed <= 100:
            raise ValueError("start_tank_at_power: left_speed must be between -100 and 100 inclusive.")

        if right_speed is None:
            right_speed = self.default_speed

        if not isinstance(right_speed, int):
            raise TypeError("right_speed must be a integer")

        if not -100 <= right_speed <= 100:
            raise ValueError("start_tank_at_power: right_speed must be between -100 and 100 inclusive.")

        print("MotorPair::start_tank_at_power")

    def get_default_speed(self) -> int:
        """ Retrieves the default motor speed.

        Returns
        -------
        int
            The default motor speed.
        """

        print("MotorPair::get_default_speed")
        return self.default_speed

    def set_motor_rotation(self, amount: float = 17.6, unit: str = 'cm'):
        """ Sets the ratio of one motor rotation to the distance traveled.

        If there are no gears used between the motors and the wheels of the Driving Base, the
        "amount" is the circumference of one wheel.

        Calling this method does not affect the Driving Base if it’s already running. It will
        only have an effect the next time one of the move or start methods is used.

        Parameters
        ----------
        amount : float
            The distance that the Driving Base moves when both motors move one rotation each.
        unit : str
            The unit of measurement specified for the "amount" parameter.

        Raises
        ------
        TypeError
            amount is not a number or unit is not a string.
        ValueError
            unit is not one of the allowed values.
        """
        if not isinstance(amount, float):
            raise TypeError("amount must be a float")

        if not isinstance(unit, str):
            raise TypeError("unit must be a str")

        if unit not in valid_motor_rotation_unit_settings:
            raise ValueError("set_motor_rotation: unit must be one of %r." % valid_motor_rotation_unit_settings)

        self.motor_rotation = {amount, unit}
        print("MotorPair::set_motor_rotation")

    def set_default_speed(self, speed: int = 100):
        """ Sets the default motor speed.

        If speed is outside the allowed range, the value will be set to "-100" or "100"
        depending on whether the value is positive or negative.

        Setting the speed will not have any effect until one of the move or start methods
        is called, even if the Driving Base is already moving.

        Parameters
        ----------
        speed : int
            The default motor speed.

        Raises
        ------
        TypeError
            speed is not a number.
        ValueError
            speed is in the acceptable range.

        """

        if not isinstance(speed, int):
            raise TypeError("speed must be a integer")

        if not -100 <= speed <= 100:
            raise ValueError("set_default_speed: speed must be between -100 and 100 inclusive.")

        self.default_speed = speed
        print("MotorPair::set_default_speed")

    def set_stop_action(self, action: str = "coast"):
        """ Sets the motor action that will be used when the Driving Base stops.

        If the action is "brake," the motors will stop quickly and be allowed to turn freely.

        If the action is "hold," the motors will actively hold their current position and
        cannot be turned manually.

        If the action is set to "coast," the motors will stop slowly and can be turned freely.

        Setting the "stop" action does not take immediate effect on the motors. The setting will
        be saved and used whenever stop() is called or when one of the move methods has completed
        without being interrupted.

        Parameters
        ----------
        action : str
            The desired action of the motors when the Driving Base stops.

        Raises
        ------
        TypeError
            action is not a string.
        ValueError
            action is not one of the allowed values.
        """

        if not isinstance(action, str):
            raise TypeError("action must be a str")

        if action not in valid_motor_stop_actions:
            raise ValueError("set_stop_action: action must be one of %r." % valid_motor_stop_actions)

        self.stop_action = action

        print("MotorPair::set_stop_action")



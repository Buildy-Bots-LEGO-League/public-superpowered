from spike import PrimeHub, ColorSensor, Motor, MotorPair, LightMatrix
from spike.control import Timer

# Define Global instances of all the parts of the robot we interact with
hub = PrimeHub()
drive_motor_pair = MotorPair('A', 'B')
side_attachment_motor = Motor('E')
top_attachment_motor = Motor('F')
left_sensor = ColorSensor('C')
right_sensor = ColorSensor('D')
right_drive_motors = Motor('B')
light_matrix = hub.light_matrix

timer = Timer()

"""
    ***********************************************
    * Functions for movement
    ***********************************************
"""


def init_movement():
    """ Initialize anything needed to move the robot """
    # Set the yaw angle to zero.This will set the direction of the robot
    # when init_movement is called to be "NORTH" or heading 0.
    hub.motion_sensor.reset_yaw_angle()


def get_heading():
    """ Get the current heading of the robot
    Returns
    -------
    int
        The heading of the robot from 0 to 360 where 0 is due north, 90 is due east, 180 is
        due south, and 270 is due west.
    """
    heading = hub.motion_sensor.get_yaw_angle()
    if heading < 0:
        heading += 360
    return heading


def set_heading(heading=0, speed=30):
    """ Turn the robot to the specified heading at the specified speed
    Parameters
    ----------
    heading : int
        The desired heading at the end of the turn (default 0)
    speed : int
        The speed to turn (default 100)
    """

    # Tuning variables
    acceptable_error = 3# The number of degrees we need to be within the target
    stop_error_setting = 5# A control to adjust when the robot stops turning
    minimum_speed = 10# The lowest speed to continue trying to correct the error

    # Calculate an acceptable point to stop turning based on the speed of the turn
    allowed_error = stop_error_setting * (speed / 100)

    # Flag to indicate if the robot should continue to turn
    keep_turning = True
    while keep_turning:
        # The actual turn speed with be positive or negative depending on which way we should turn.
        actual_turn_speed = speed * determine_turn_direction(heading)

        # Start turning
        drive_motor_pair.start_tank(actual_turn_speed, actual_turn_speed * -1)

        # Decide is we should keep turning based on the current heading being between the
        # desired heading + and - the allowed error.
        keep_turning = not (heading - allowed_error <= get_heading() <= heading + allowed_error)

    # Stop turning
    drive_motor_pair.stop()

    # Double check to make sure we are inside the acceptable error margin.If we are not inside
    # the acceptable error margin then we should try to turn to the desired heading again up at
    # a slower speed.Only do this if the speed is above the minimum speed to avoid an infinite
    # loop.
    if abs(get_heading() - heading) > acceptable_error and speed > minimum_speed:
        set_heading(heading, int(speed / 2))


def determine_turn_direction(goal_heading):
    """ Determine the direction to turn based on the current heading and the desired goal heading
    Parameters
    ----------
    goal_heading : int
        The heading the robot will be turning to
    Returns
    -------
    int
        Positive 1 if the robot should turn clockwise or negative if the robot should turn
        counter-clockwise. """

    current_heading = get_heading()
    clockwise = 1
    counter_clockwise = -1

    if current_heading < goal_heading:
        if goal_heading - current_heading < 180:
            return clockwise
        else:
            return counter_clockwise
    else:
        if current_heading - goal_heading < 180:
            return counter_clockwise
        else:
            return clockwise


def drive_distance(heading=0, distance=10, power=50, correction_factor=3):
    """ Drive at a heading for a given distance in centimeters
    Parameters
    ----------
    heading : int
        The heading which the robot should drive (default 0)
    distance : int
        The distance to travel in centimeters (default 10)
    power : int
        The power to move (default 50%)
    correction_factor : int
        A number to determine if the robot is drifting
    """

    # Calculate the number of centimeters is one degree of movement of the motor
    cm_per_degree = (27.6 / 360) * 1.0

    set_heading(heading)
    right_drive_motors.set_degrees_counted(0)
    traveled = 0
    if (distance > 0):
        while traveled < distance:
            drive_heading(heading, power, correction_factor)
            ##
            traveled = cm_per_degree * right_drive_motors.get_degrees_counted()
    else:
        while traveled < distance * -1:
            drive_heading(heading, -1 * power, correction_factor)
            traveled = cm_per_degree * abs(right_drive_motors.get_degrees_counted())
    drive_motor_pair.stop()


def drive_heading(heading=0, power=50, correction_factor=3, turn_first=False):
    """ Move towards a heading
    Parameters
    ----------
    heading : int
        The desired heading
    power : int
        The power to move
    correction_factor : int
        A number to determine if the robot is drifting
    """

    if (turn_first):
        set_heading(heading)

    # Calculate how far off of the desired heading the robot is currently pointing
    error = get_heading() - heading
    if abs(error) > 180:
        # In this case due north is between the desired and actual heading
        if error > 0:
            error = error - 360
        if error < 0:
            error = error + 0

    correction = error * correction_factor
    drive_motor_pair.start_tank_at_power(int(power - correction), int(power + correction))


north = 0
north_east = 45
east = 90
south_east = 135
south = 180
south_west = 225
west = 270
north_west = 315


init_movement()
drive_distance(north, 200, 100)
drive_distance(north, 10, 20)
raise SystemExit

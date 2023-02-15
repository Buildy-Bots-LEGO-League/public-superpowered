from spike import PrimeHub, ColorSensor, Motor, MotorPair, LightMatrix
from spike.control import Timer, wait_for_seconds

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


def stop_on_line(timeout=10):
    """ Stop the robot when the left sensor sees black
        Note this function assumed the robot is moving
        Parameters
        ----------
        timeout : int
            The number of seconds before the function will stop without seeing the line.
        Returns
        -------
        boolean
            True if the black line was found, false if the timeout was reached
    """

    light_matrix.show_image("CHESSBOARD")
    timer.reset()

    while True:
        print(left_sensor.get_reflected_light())
        if left_sensor.get_reflected_light() < 50.0:
            drive_motor_pair.stop()
            light_matrix.show_image("HAPPY")
            return True
        if timer.now() > timeout:
            drive_motor_pair.stop()
            print(timeout)
            light_matrix.show_image("ANGRY")
            return False


def follow_for_time(duration=5, base_power=20, correction_factor=0.3):
    """ Follow a line which is just in front of the robot for a given number of seconds
        using the left sensor.
        Parameters
        ----------
        duration : int
            The number of seconds to follow the line (default 5 seconds)
        base_power : int
            The power to apply to the motors (default 40%)
        correction_factor : float
            A number to determine how frequently the robot should turn back. (default 0.3)
    """
    drive_motor_pair.start(0, 30)
    stop_on_line()
    timer.reset()
    while timer.now() < duration:
        error = left_sensor.get_reflected_light() - 50
        correction = error * correction_factor
        drive_motor_pair.start_tank_at_power(int(base_power + correction), int(base_power - correction))
    drive_motor_pair.stop()


def follow_until_line(base_power=40, correction_factor=0.3):
    """ Follow a line which is just in front of the robot using the left sensor until the
        right sensor detects a black line.
        Parameters
        ----------
        base_power : int
            The power to apply to the motors (default 40%)
        correction_factor : float
            A number to determine how frequently the robot should turn back. (default 0.3)
    """
    drive_motor_pair.start(0, 30)
    stop_on_line()
    while right_sensor.get_reflected_light() > 50:
        error = left_sensor.get_reflected_light() - 50
        correction = error * correction_factor
        drive_motor_pair.start_tank_at_power(int(base_power + correction), int(base_power - correction))
    drive_motor_pair.stop()


def drive_time(heading=0, duration=5, power=60, correction_factor=3):
    """ Drive at a heading for a given number of seconds
    Parameters
    ----------
    heading : int
        The heading which the robot should drive (default 0)
    duration : int
        The time the robot should spend driving (default 5 seconds)
    power : int
        The power to move. (default 50%)
    correction_factor : int
        A number to determine if the robot is drifting.
    """

    # Turn the robot in the direction we want to move
    set_heading(heading)

    timer.reset()
    while timer.now() < duration:
        drive_heading(heading, power, correction_factor)
    drive_motor_pair.stop()


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

def drive_until_line(heading = 0, power = 50, correction_factor = 3):
    """ Drive at a givin speed until a line
    Parameters
    ----------
    power : int
        The power to move (default 50%)
    correction_factor : int
        A number to determine if the robot is drifting
    """
    if(left_sensor.get_reflected_light() < 50):
        drive_distance(heading, 3, power, correction_factor)

    while left_sensor.get_reflected_light() > 50:
        drive_heading(heading, power, correction_factor)
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


"""
    ***********************************************
    * Functions for attachments
    ***********************************************
"""

"""
    The FLYSWATTER
    This attachment uses the top motor to raise and lower parts in front of the robot
"""


def init_fly_swatter():
    """ Initialize the fly swatter attachment.
    The attachment should be manually adjusted to be flow on the surface in front of the robot.
    Fully down will be set to 0 degrees
    """
    top_attachment_motor.set_degrees_counted(0)


def position_fly_swatter(setting=360, speed=75):
    """ Set the position of the flyswatter attachment
        0 = All the way down
        360 = All the way up
        Parameters
        ----------
        setting : int
            The desired position
        speed : int
            The speed to move the fly swatter
    """
    current = top_attachment_motor.get_degrees_counted()

    # Only allow values between 0 and 360
    if setting > 360:
        setting = 360
    if setting < 0:
        setting = 0

    # A hire setting is actually a lower turn so flip the setting
    setting = setting * -1

    if current > setting:
        # Move down
        top_attachment_motor.run_to_degrees_counted(setting, speed * -1)
    else:
        # Move up
        top_attachment_motor.run_to_degrees_counted(setting, speed)


"""
    The SWORD
    This attachment uses the side motor.
"""


def init_sword():
    """ Initialize the sword attachment
    The attachment should be manually adjusted upward as far as possible
    """
    side_attachment_motor.set_degrees_counted(0)


def position_sword(setting=0, speed=50):
    """ Set the position of the sword attachment
        0 = All the way down
        90 = All the way up
        Parameters
        ----------
        setting : int
            The desired position of the attachment
        speed : int
            The speed which the attachment should move
    """
    min_setting = 0
    # TODO: determine action max value for down
    max_setting = 150

    if setting < min_setting:
        setting = min_setting
    if setting > max_setting:
        setting = max_setting

    if side_attachment_motor.get_degrees_counted() > setting:
        side_attachment_motor.run_to_degrees_counted(setting, speed * -1)
    else:
        side_attachment_motor.run_to_degrees_counted(setting, speed)


"""
    The DISPENSER
    This attachment uses the top attachment motor to dispense energy units
"""

def init_dispenser():
    top_attachment_motor.set_degrees_counted(0)

def position_dispenser(position=0,power=50):
    top_attachment_motor.run_to_degrees_counted(position,power)

"""
    The DROPPER
    This attachment uses the side attachment motor deliver packages.
"""

def init_dropper():
    top_attachment_motor.set_degrees_counted(0)

def drop(position = 0, speed = 50):
    top_attachment_motor.run_to_degrees_counted(position,speed)
    wait_for_seconds(.5)
    top_attachment_motor.run_to_degrees_counted(0,speed)
"""
    The CLAW
    This attachment uses the side attachment motor grab.
"""

# TODO: Initialize claw
# TODO: Operate claw

"""
    ***********************************************
    * Program sequences
    ***********************************************
"""
north = 0
north_east = 45
east = 90
south_east = 135
south = 180
south_west = 225
west = 270
north_west = 315

init_movement()
init_dispenser()
init_dropper()

drive_distance(north,20)
set_heading(west)
drive_distance(west,30)
set_heading(north_west)
drive_distance(north_west,10,30)
drop(70,10)
drop(0,100)
drive_distance(north_west,-70)
raise SystemExit

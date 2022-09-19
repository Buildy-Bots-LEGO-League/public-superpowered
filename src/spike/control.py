from time import sleep
import time
from inspect import signature

from .operator import equal_to

"""Functions to control program flow"""


def wait_for_seconds(seconds: float):
    """Waits for a specified number of seconds before continuing the program

    Parameters
    ----------
    seconds : float
        The number of seconds to wait.

    Raises
    ------
    TypeError
        seconds is not a number
    ValueError
        seconds is not at least 0

    """

    if not isinstance(seconds, float) and not isinstance(seconds, int):
        raise TypeError("wait_for_seconds seconds must be a number")
    if seconds < 0:
        raise ValueError("wait_for_seconds seconds must be at least 0")

    print("wait_for_seconds")
    sleep(seconds)\



def wait_until(get_value_function: callable, operator_function: callable = equal_to, target_value=True):
    """Waits until the condition is true before continuing with the program.

    Parameters
    ----------
    get_value_function : callable
        A function that returns the current value to be compared to the target value.
    operator_function : callable
        A function that compares two arguments. The first argument will be the result of get_value_function(),
        and the second argument will be target_value. The function will compare both values and return the result.
    target_value : any
        Object that can be compared by operator_function.

    Raises
    ------
    TypeError
        get_value_function or operator_function is not callable or operator_function does not compare two arguments.
    """

    if not callable(get_value_function):
        raise TypeError("wait_until get_value_function must be a callable")
    if not callable(operator_function):
        raise TypeError("wait_until operator_function must be a callable")

    if len(signature(operator_function).parameters) != 2:
        raise TypeError("wait_until operator_function must take two arguments")

    if isinstance(signature(operator_function).return_annotation, bool):
        raise TypeError("wait_until operator_function must return bool")

    while not operator_function(get_value_function, target_value):
        sleep(0.25)


class Timer:
    """ Following are all the functions that are linked to the Timer. """

    def __init__(self):
        """ Constructor for Timer """
        self.start_time = int(time.time())
        print("Timer::__init__")

    start_time = 0

    def reset(self):
        """ Sets the Timer to "0." """
        self.start_time = int(time.time())
        print("Timer::reset")

    def now(self) -> int:
        """ Retrieves the "right now" time of the Timer.

        Returns
        -------
        int
            The current time, specified in seconds.

        """

        print("Timer::now")
        return int(time.time()) - self.start_time

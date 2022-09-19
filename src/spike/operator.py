""" Functions for comparing objects """


def greater_than(lhs, rhs) -> bool:
    """ Is left hand side greater than the right hand side?

    Parameters
    ----------
    lhs : any
        The left hand side of the comparison
    rhs : any
        The right hand side of the comparison

    Returns
    -------
    bool
        True if the left hand side is greater than the right hand side, otherwise false.

    """

    return lhs > rhs


def greater_than_or_equal_to(lhs, rhs) -> bool:
    """ Is left hand side greater than of equal to the right hand side?

    Parameters
    ----------
    lhs : any
        The left hand side of the comparison
    rhs : any
        The right hand side of the comparison

    Returns
    -------
    bool
        True if the left hand side is greater than or equal to the right hand side, otherwise false.

    """
    return lhs >= rhs


def less_than(lhs, rhs) -> bool:
    """ Is left hand side less than the right hand side?

    Parameters
    ----------
    lhs : any
        The left hand side of the comparison
    rhs : any
        The right hand side of the comparison

    Returns
    -------
    bool
        True if the left hand side is less than the right hand side, otherwise false.

    """
    return lhs < rhs


def less_than_or_equal_to(lhs, rhs) -> bool:
    """ Is left hand side less than or equal to the right hand side?

    Parameters
    ----------
    lhs : any
        The left hand side of the comparison
    rhs : any
        The right hand side of the comparison

    Returns
    -------
    bool
        True if the left hand side is less than or equal to the right hand side, otherwise false.

    """
    return lhs <= rhs


def equal_to(lhs, rhs) -> bool:
    """ Is left hand side equal to the right hand side?

    Parameters
    ----------
    lhs : any
        The left hand side of the comparison
    rhs : any
        The right hand side of the comparison

    Returns
    -------
    bool
        True if the left hand side is equal to the right hand side, otherwise false.

    """
    return lhs == rhs


def not_equal_to(lhs, rhs) -> bool:
    """ Is left hand side not equal to the right hand side?

    Parameters
    ----------
    lhs : any
        The left hand side of the comparison
    rhs : any
        The right hand side of the comparison

    Returns
    -------
    bool
        True if the left hand side not equal to the right hand side, otherwise false.

    """
    return lhs != rhs


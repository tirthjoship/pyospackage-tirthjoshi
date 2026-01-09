"""Example module with simple mathematical functions."""


def add_num(a: int, b: int) -> int:
    """
    Add two numbers.

    Parameters
    ----------
    a : int
        The first number to be added.
    b : int
        The second number to be added.

    Returns
    -------
    int
        The sum of the two input numbers (a + b).

    Examples
    --------
    >>> add_num(3, 5)
    8
    >>> add_num(-2, 7)
    5
    """
    return a + b


def subtract_num(a: int, b: int) -> int:
    """
    Subtract two numbers.

    Parameters
    ----------
    a : int
        The number to subtract from.
    b : int
        The number to subtract.

    Returns
    -------
    int
        The difference of the two input numbers (a - b).

    Examples
    --------
    >>> subtract_num(10, 3)
    7
    >>> subtract_num(5, 8)
    -3
    """
    return a - b

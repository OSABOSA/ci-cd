"""# przykladowe funkcje utils.py"""


def add(a: int, b: int) -> int:
    """
    Adds two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Subtracts one integer from another.

    Args:
        a (int): The integer to be subtracted from.
        b (int): The integer to subtract.

    Returns:
        int: The result of the subtraction.
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of the two integers.
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Divides one integer by another.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of the division.
    """
    return a / b

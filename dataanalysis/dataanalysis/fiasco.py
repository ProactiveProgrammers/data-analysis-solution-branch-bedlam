"""Create a fiasco in the functions and branches of a program."""

from functools import wraps

import inspect

import math

LITTLE = "little"
SINGLE_BLANK_SPACE = " "


def convertToNumber(s):
    """Convert from a textual representation to a numerical value."""
    return int.from_bytes(s.encode(), "little")


def convertFromNumber(n):
    """Convert from a numerical value to a textual representation."""
    return n.to_bytes(math.ceil(n.bit_length() / 8), LITTLE).decode()


def createfiasco(function):
    """Define a fiasco function that can observe and control function execution."""

    @wraps(function)
    def wrap(*args, **kwargs):
        function_name = function.__name__
        function_module = inspect.getmodule(function)
        function_id = convertToNumber(function_name + SINGLE_BLANK_SPACE + str(function_module))
        function_details_from_id = convertFromNumber(function_id)
        print(
            f"function {function_name} found in module {function_module} has id {function_id}"
        )
        print(f"reverse engineered function {function_details_from_id}")
        result = function(*args, **kwargs)
        return result

    return wrap

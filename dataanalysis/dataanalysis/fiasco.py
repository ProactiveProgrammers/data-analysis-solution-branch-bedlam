"""Create a fiasco in the functions and branches of a program."""

from functools import wraps

import inspect

import math

LITTLE = "little"
SINGLE_BLANK_SPACE = " "


def convert_to_number(textual):
    """Convert from a textual representation to a numerical value."""
    return int.from_bytes(textual.encode(), "little")


def convert_from_number(number):
    """Convert from a numerical value to a textual representation."""
    return number.to_bytes(math.ceil(number.bit_length() / 8), LITTLE).decode()


def createfiasco(function):
    """Define a fiasco function that can observe and control function execution."""

    @wraps(function)
    def wrap(*args, **kwargs):
        function_name = function.__name__
        function_module = inspect.getmodule(function)
        function_id = convert_to_number(function_name + SINGLE_BLANK_SPACE + str(function_module))
        function_details_from_id = convert_from_number(function_id)
        print(
            f"function {function_name} found in module {function_module} has id {function_id}"
        )
        print(f"reverse engineered function {function_details_from_id}")
        result = function(*args, **kwargs)
        return result

    return wrap

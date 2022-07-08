"""Create a fiasco in the functions of a program."""

from functools import wraps

import json
import inspect
import math

LITTLE = "little"
SINGLE_BLANK_SPACE = " "

fiasco_tracker = {}

fiascoified_function_id = None


def convert_to_number(textual):
    """Convert from a textual representation to a numerical value."""
    return int.from_bytes(textual.encode(), "little")


def convert_from_number(number):
    """Convert from a numerical value to a textual representation."""
    return number.to_bytes(math.ceil(number.bit_length() / 8), LITTLE).decode()


def save_tracker():
    """Save the function fiasco tracker."""
    print("Saving the tracker")
    with open("fiasco.json", "w") as fiasco_json_file:
        json.dump(fiasco_tracker, fiasco_json_file)


def read_tracker():
    """Read the function fiasco tracker."""
    print("Reading the tracker")
    fiasco_dict = {}
    with open("fiasco.json", "r") as fiasco_json_file:
        fiasco_dict = json.load(fiasco_json_file)
    return fiasco_dict


def createfiasco(function):
    """Define a fiasco function that can observe and control function execution."""

    @wraps(function)
    def wrap(*args, **kwargs):
        # extract the name of the function
        function_name = function.__name__
        # extract the module of the function
        function_module = inspect.getmodule(function)
        # convert the name and module of the function into an integer identifier
        # note that it may not be guaranteed that this number is unique
        function_id = convert_to_number(
            function_name + SINGLE_BLANK_SPACE + str(function_module)
        )
        function_details_from_id = convert_from_number(function_id)
        # create a key value pair of (function_id, False) to indicate that this
        # specific function has not yet been fiasco-ified (i.e., turned off) during
        # the execution of the test suite
        fiasco_tracker[function_id] = False
        print(
            f"function {function_name} found in module {function_module} has id {function_id}"
        )
        print(f"reverse engineered function {function_details_from_id}")
        # the current function is supposed to be fiascoified, which means
        # that it should not be executed; return None instead of running
        # the function and returning its actual return value
        if fiascoified_function_id == function_id:
            print(
                f"WILL NOT RUN THIS FUNCTION! + {convert_from_number(fiascoified_function_id)}"
            )
            return None
        # the current function is not supposed to be fiascoified, which means
        # that it should be run normally and then its return value returned;
        # from the perspective of the function and its program, there should be
        # no evidence that this decorator was actually executed
        else:
            result = function(*args, **kwargs)
            return result

    return wrap

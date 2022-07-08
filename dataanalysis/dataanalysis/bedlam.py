"""Create a bedlam in the branches of a program."""

import contextlib
import json


def save_tracker():
    """Save the branch bedlam tracker."""
    print("Saving the tracker")
    print(Bedlam.bedlam_tracker)
    with open("bedlam.json", "w") as bedlam_tracker_file:
        json.dump(Bedlam.bedlam_tracker, bedlam_tracker_file)


@contextlib.contextmanager
def createbedlam():
    print("Before execution")
    yield
    # pass
    print("After execution")


class SuppressExc(object):
    def __enter__(self):
        print("Entering branch")
        return self

    def __exit__(self, ex_type, ex_instance, traceback):
        if ex_instance:
            print("Suppressing exception: % s." % ex_instance)
        return True


class Bedlam(object):

    bedlam_tracker = {}

    def __init__(self, identifier):
        """Initialize a new instance of the Bedlam."""
        self.identifier = identifier
        Bedlam.bedlam_tracker[identifier] = False

    def __enter__(self):
        """Before the execution of the statement in the context."""
        print("before context")
        Bedlam.bedlam_tracker[self.identifier] = False
        return self

    def __exit__(self, exit_type, exit_instance, traceback):
        """After the execution of the statement in the context."""
        print("after context")

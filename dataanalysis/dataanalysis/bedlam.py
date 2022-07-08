"""Create a bedlam in the branches of a program."""

import contextlib
import json


bedlam_tracker = {}

bedlamified_branch_id = None


def save_tracker():
    """Save the branch bedlam tracker."""
    print("Saving the bedlam tracker")
    print(bedlam_tracker)
    with open("bedlam.json", "w") as bedlam_tracker_file:
        json.dump(bedlam_tracker, bedlam_tracker_file)


def read_tracker():
    """Read the branch bedlam tracker."""
    print("Reading the bedlam tracker")
    bedlam_dict = {}
    with open("bedlam.json", "r") as bedlam_json_file:
        bedlam_dict = json.load(bedlam_json_file)
    return bedlam_dict


def register_bedlam(identifier):
    """Register a specified location in an if statement."""
    print(f"REGISTER: {identifier}")
    bedlam_tracker[identifier] = False
    print(bedlam_tracker)
    return True


def skip_branch(branch_identifier):
    """Skip a branch if the branch identifier matches."""
    print(
        f"BEDLAM: in the skip_branch function for {branch_identifier} with current branch to bedlamify as {bedlamified_branch_id}"
    )
    if int(branch_identifier) == int(bedlamified_branch_id):
        print("BEDLAM: going to skip the branch!")
        return False
    print("BEDLAM: not going to skip the branch!")
    return True


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

"""Control the execution of the test suite."""

import sys

import pytest

from dataanalysis import fiasco
from dataanalysis import bedlam

TRACE_INTO = ["compute_mean"]


def cause_testing_fiasco():
    """Cause a testing fiasco."""
    print("Run the test suite")
    fiasco_tracker = fiasco.read_tracker()
    run = 1
    print("START FUNCTION FIASCO")
    for fiascoified_function_id in fiasco_tracker:
        print(
            f"RUN {run}: RUN TEST SUITE AND STOP {fiasco.convert_from_number(int(fiascoified_function_id))}"
        )
        fiasco.fiascoified_function_id = int(fiascoified_function_id)
        pytest.main(["tests", "-s"])
        run += 1
    print(f"END FUNCTION FIASCO AFTER {run-1} runs")
    print(f"FUNCTION FIASCO TRACKER:\n {fiasco_tracker}")


def cause_branch_bedlam():
    """Cause a branch bedlam."""
    # sys.settrace(trace_calls)
    bedlam_tracker = bedlam.read_tracker()
    run = 1
    print("START BRANCH BEDLAM")
    for bedlamified_conditional_id in bedlam_tracker:
        print(f"RUN {run}: RUN TEST SUITE AND STOP {bedlamified_conditional_id}")
        bedlam.bedlamified_branch_id = bedlamified_conditional_id
        pytest.main(["tests", "-s"])
        run += 1
    print(f"END BRANCH BEDLAM AFTER {run-1} runs")
    print(f"BRANCH BEDLAM TRACKER:\n {bedlam_tracker}")
    pytest.main(["tests", "-s"])


def trace_lines(frame, event, arg):
    if event != "line":
        return
    co = frame.f_code
    print(f"code = {co}")
    func_name = co.co_name
    line_no = frame.f_lineno
    print(f"frame = {frame}")
    filename = co.co_filename
    print("TRACE  %s line %s" % (func_name, line_no))


def trace_calls(frame, event, arg):
    if event != "call":
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == "write":
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    print("Call to %s on line %s of %s" % (func_name, line_no, filename))
    if func_name in TRACE_INTO:
        # Trace into this function
        return trace_lines
    return

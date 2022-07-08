"""Control the execution of the test suite."""

import pytest

from dataanalysis import fiasco


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

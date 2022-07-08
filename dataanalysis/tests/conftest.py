"""Define a globally accessible fixture."""

import pytest

from dataanalysis import bedlam
from dataanalysis import fiasco


@pytest.fixture(scope="session", autouse=True)
def session_setup_teardown():
    """Execute arbitrary operations before and after running a test suite."""
    print("Before test suite execution")
    yield
    fiasco.save_tracker()
    bedlam.save_tracker()
    print("After test suite execution")


@pytest.fixture(scope="function", autouse=True)
def function_setup_teardown(request):
    """Execute arbitrary operations before and after running a test suite."""
    test_name = request.function.__name__
    print(f"Before test case execution: {test_name}")
    yield
    print("After test case execution")

"""Define a globally accessible fixture."""

import pytest


@pytest.fixture(scope='session', autouse=True)
def session_setup_teardown():
    print("Before test suite execution")
    yield
    print("After test suite execution")

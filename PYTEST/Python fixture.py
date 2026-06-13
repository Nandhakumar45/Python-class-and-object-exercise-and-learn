# Fixture means - Re usable function, it is like set up an environment. No need to mention "test" keyword where we have to denote..
import pytest


@pytest.fixture
def setup():
    print("setup enviroment ")


def test_one(setup):
    print("I belong to test 1")


def test_two(setup):
    print("I belong to test 2")


def test_three(setup):
    print("I belong to test 3")

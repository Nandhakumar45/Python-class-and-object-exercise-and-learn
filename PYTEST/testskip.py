#to skip the test function. this is also called decorator  in pytest

#@pytest.mark.skip

import pytest

def test_loginbyemail():
    print("I belong to email test")
    assert 1==1

@pytest.mark.skip
def test_loginbyfacebook():
    print("I belong to facebook test")
    assert 1 == 1

def test_loginbygmail():
    print("I belong to gmail test")
    assert 1 == 1

def test_loginbyemail2():
    print("I belong to email test2")
    assert True == True

@pytest.mark.skip
def test_loginbygmail2():
    print("I belong to gmail test2")
    assert True == True

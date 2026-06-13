# grouping the test is one of the best method to classify what are test need to execute in sanity and regression testing.
""" grouping test
test_login by email-sanity and regression
test-login by facebook- sanity
test-login by phone - regression
test-signup by email - sanity, regression
tset-signup by facebook - regression
test-signup by phone - sanity
test-payment in dollar - sanity , regression
test-payment in rupees - regression

1. Run only sanity, regression and sanity and regression commend
"""
import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_login_by_email():
    print("I belong to login_by_email")
    assert 1 == 1


@pytest.mark.sanity
def test_login_by_facebook():
    print("I belong to facebook test")
    assert 1 == 1


@pytest.mark.regression
def test_login_by_phone():
    print("I belong to login_by_phone")
    assert 1 == 1


@pytest.mark.sanity
@pytest.mark.regression
def test_signup_by_facebook():
    print("I belong to signup_by_facebook")
    assert True == True


@pytest.mark.sanity
def test_signup_by_phone():
    print("I belong to signup_by_phone")
    assert True == True


@pytest.mark.sanity
@pytest.mark.regression
def test_payment_in_dollar():
    print("I belong to payment_in_dollar")
    assert True == True


@pytest.mark.regression
def test_payment_in_rupees():
    print("I belong to payment in rupees")
    assert True == True

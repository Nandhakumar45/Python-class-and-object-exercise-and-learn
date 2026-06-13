'''  The main use of the to ordering the pytest in the sequential way ordering preconiton. First we need to install plugin

pip install pytest-order

'''

import pytest


# @pytest.mark.order(1)
# def test_login():
#     print('Testing login')
#
#
# @pytest.mark.order(3)
# def test_add_item():
#     print('Testing add_item')
#
#
# @pytest.mark.order(2)
# def test_remove_item():
#     print('Testing remove_item')
#
# #'''example 2'''
#
#
# @pytest.mark.order(3)
# def test_login():
#     print('Testing login_1')
#
#
# @pytest.mark.order(2)
# def test_add_item():
#     print('Testing add_item_2')
#
#
# @pytest.mark.order(1)
# def test_remove_item():
#     print('Testing remove_item_3')


# approach 2


# @pytest.mark.order(1)
# def test_login():
#     print('Testing login')
#
#
# @pytest.mark.order(before="checkout")
# def test_add_item():
#     print('Testing add_item')
#
#
# @pytest.mark.order(after="add_item")
# def test_checkout():
#     print('Testing checkout')

# approach 3

@pytest.mark.order("first")
def test_login():
    print('Testing login')


@pytest.mark.order()
def test_add_item():
    print('Testing add_item')


@pytest.mark.order("last")
def test_checkout():
    print('Testing checkout')

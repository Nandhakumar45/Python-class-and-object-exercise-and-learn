# the main use of this test to run the test methods in parallel and the mentioned commend is required to run the parallel script "pip install pytest-xdist"

''' python -m pytest .\PYTEST\test_parallel.py -v -s -n 2 this is the commend to run the script at end of the commend  we have mentioned 2 which represent the number workers '''



def test_one():
    print("Running test one")
    assert 1 == 1


def test_two():
    print("Running test two")
    assert 2 == 2


def test_three():
    print("Running test three")
    assert 3 == 3


def test_four():
    print("Running test four")
    assert 4 == 4

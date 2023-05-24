from to_be_tested.python_script import factorial


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(-2) == "The number can not be negative."
    assert factorial(1.5) == "Only integer numbers are accepted."


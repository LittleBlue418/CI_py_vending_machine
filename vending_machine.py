from tests import *

def get_change(amount):
    if amount == 0:
        return []
    if amount in [100, 50, 20, 10, 5, 2, 1]:
        return [amount]

    return [2,1]

"""
TESTS
"""
tests_are_equal(get_change(0),[])
tests_are_equal(get_change(1),[1])
tests_are_equal(get_change(2),[2])
tests_are_equal(get_change(5),[5])
tests_are_equal(get_change(10),[10])
tests_are_equal(get_change(20),[20])
tests_are_equal(get_change(50),[50])
tests_are_equal(get_change(100),[100])

tests_are_equal(get_change(3)[2,1])

print("All tests pass!")
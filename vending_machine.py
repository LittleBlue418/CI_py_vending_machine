from tests import *

def get_change(amount):
    if amount == 0:
        return []
    if amount in [100, 50, 20, 10, 5, 2, 1]:
        return [amount]

    change = []
    # If the coin is less than or equal to the amount then we should add it to the change
    for coin in [100, 50, 20, 10, 5, 2, 1]:
        if coin <=amount:
            change.append(coin)

    return change

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

tests_are_equal(get_change(3),[2,1])
tests_are_equal(get_change(7),[5,2])

print("All tests pass!")
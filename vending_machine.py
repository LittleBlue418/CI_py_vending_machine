from tests import *

coins = [100, 50, 20, 10, 5, 2, 1]

def get_change(amount):
    change = []
    # If the coin is less than or equal to the amount then we should add it to the change
    for coin in coins:
        # while statement here means it will continue to itterate to give multiples of the same denomination (for 9)
        while coin <=amount:
            # deducing the amount of the coin from the amount that we sent in
            amount -= coin
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
tests_are_equal(get_change(9), [5,2,2])

print("All tests pass!")
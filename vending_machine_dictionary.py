from tests import *

usd_coin_reserve = {
    100 : 1,
    50 : 20,
    25 : 20,
    10 : 20,
    5 : 20,
    1 : 20,
}

eur_coin_reserve = {
    100 : 2,
    50 : 2,
    20 : 2,
    10 : 2,
    5 : 2,
    2 : 2,
    1 : 2,
}

# defaults to using euro coins
def get_change(amount, coins=eur_coin_reserve):
    initial_amount = amount
    change = []
    # If the coin is less than or equal to the amount then we should add it to the change
    for denomination in sorted(coins.keys(), reverse=True):
        value = (coins[denomination])
        # while statement here means it will continue to itterate to give multiples of the same denomination (for 9)
        while denomination <= amount and value > 0:
            # deducing the amount of the coin from the amount that we sent in
            amount -= denomination
            change.append(denomination)
            value -= 1
    if sum(change) == initial_amount:
        return change
    else:
        return "Error: out of change!"

print(get_change(500))


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

tests_are_equal(get_change(35, usd_coin_reserve),[25,10])

#Over riding the default euro coin reserve and providing a new dictionary
tests_are_equal(get_change(5, {2: 1, 1: 4}), [2,1,1,1])
tests_are_equal(get_change(30, {25:1, 5:1}), [25,5])


print("All tests pass!")

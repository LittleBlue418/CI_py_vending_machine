list_of_numbers = [1,2,3,4,5,6,7,8]

def number_of_evens(numbers):
    return 0

def tests_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def tests_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)

def test_is_between(item):
    assert item > -1 and item < 101, "{0} is not between 0 and 100".format(item)

tests_not_equal(number_of_evens(list_of_numbers), 2)
test_is_in(list_of_numbers, 2)
test_is_between(20)
#test_not_in(list_of_numbers, 2)
#tests_are_equal(number_of_evens([1,2,3,4,5]), 2)
print("All tests padssed")
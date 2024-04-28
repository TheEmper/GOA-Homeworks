# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.


def find_it(seq):
    for num in seq:
        i = seq.count(num)
        if i % 2 != 0:
            return num
        


# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

def array_diff(a, b):
    result = []
    for num in a:
        if num not in b:
            result.append(num)
    return result

    
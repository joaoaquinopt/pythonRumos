'''
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

'''

import math
from typing import Any


def grow(arr):
    value = 1
    for exp in arr:
        value = exp * value
    return value


print(grow([1, 2, 3]))
print(grow([4, 1, 1, 1, 4]))
print(grow([2, 2, 2, 2, 2, 2]))

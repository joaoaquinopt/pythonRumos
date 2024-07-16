'''
You get an array of numbers, return the sum of all of the positives ones.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0.
'''


def positive_sum(arr):
    if not arr:
        return 0

    count = 0
    sum = 0
    while count < len(arr):
        if arr[count] > 0:
            sum += int(arr[count])
            count += 1
        else:
            sum += 0
            count += 1
    return sum


print(positive_sum([1, 2, 3, 4, 5]))

print(positive_sum([1, -2, 3, 4, 5]))

print(positive_sum([-1, 2, 3, 4, -5]))

print(positive_sum([]))

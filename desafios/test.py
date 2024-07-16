from numpy import empty


def count_positives_sum_negatives(arr):
    if not arr:
        return []

    positive_count = 0
    negative_sum = 0

    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_sum += num

    return [positive_count, negative_sum]


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -11, -12, -13, -14, -15, -16]))
print(count_positives_sum_negatives([0, 0]))
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(count_positives_sum_negatives([1]))
print(count_positives_sum_negatives([-1]))
print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(count_positives_sum_negatives([]))

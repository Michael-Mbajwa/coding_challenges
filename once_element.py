from collections import defaultdict


def once_element(arr):
    """
    Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
    find and return the non-duplicated integer.
    For example,given [6, 1, 3, 3, 3, 6, 6],return 1. Given [13, 19, 13, 13], return 19.
    Do this in O(N) time and O(1) space.
    :param arr:
    :return:
    """

    result = defaultdict(int)
    for num in arr:
        result[num] += 1

    return min(result, key=result.get)


if __name__ == "__main__":
    print(once_element([13, 19, 13, 13]))
from collections import Counter


def three_times(arr):
    # This method has time complexity O(n+m)
    """
    This problem was asked by Google.

    Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
    find and return the non-duplicated integer.

    For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

    Do this in O(N) time and O(1) space.
    :param arr:
    :return:
    """
    occ = dict()
    for integer in arr:
        if integer in occ:
            occ[integer] += 1
        else:
            occ[integer] = 1
    for key, value in occ.items():
        if value == 1:
            return key


def three_times2(arr):
    # This method has time complexity O(n)
    count = Counter(arr)
    for i in count:
        if count[i] == 1:
            return i


if __name__ == "__main__":
    print(three_times2([13, 19, 13, 13]))
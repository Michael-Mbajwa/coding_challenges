def distinct_elements_length(arr):
    """
    This problem was asked by Google.

    Given an array of elements, return the length of the longest subarray where all its elements are distinct.

    For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is
    [5, 2, 3, 4, 1].
    :return:
    """
    distinct_elements = set(arr)
    longest_sub_array = list(distinct_elements)
    result = len(longest_sub_array)

    return result


if __name__ == "__main__":
    test = distinct_elements_length([5, 1, 3, 5, 2, 3, 4, 1])
    print(test)
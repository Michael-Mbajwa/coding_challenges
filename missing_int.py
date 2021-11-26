import heapq


def first_missing_int(arr):
    # I believe this is a more appropriate solution
    """
    Given an array of integers, find the first missing positive integer in linear time and constant space.
    In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates
    and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
    You can modify the input array in-place.
    """
    if max(arr) <= 0:
        return 1
    for i in range(1, max(arr)+2):
        try:
            arr.index(i)
        except ValueError:
            return i


def first_missing_integer_2(arr):
    # This is an alternative solution for this particular problem. This code only works if we are to work within the
    # interval of (min-1, max+1) of the arr. For example an arr like [15, 14, 13, 11] will give 10 instead of 0.
    """
    Given an array of integers, find the first missing positive integer in linear time and constant space.
    In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates
    and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

    You can modify the input array in-place.
    """
    my_heap = []
    heapq.heapify(my_heap)
    for i in arr:
        if (i-1) > 0 and (i-1) not in arr and (i-1) not in my_heap:
            heapq.heappush(my_heap, i-1)
        if (i+1) > 0 and (i+1) not in arr and (i+1) not in my_heap:
            heapq.heappush(my_heap, i+1)
    return heapq.heappop(my_heap)
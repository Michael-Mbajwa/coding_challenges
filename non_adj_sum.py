def non_adj_sum(arr):
    """
    Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
    Numbers can be 0 or negative.

    For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
    since we pick 5 and 5.

    Follow-up: Can you do this in O(N) time and constant space?
    """
    sums = set()
    for i in range(len(arr)):
        n = 2
        while n < len(arr):
            if len(arr[i::n]) > 1:
                sums.add(sum(arr[i::n]))
            n += 1
    return max(sums)


print(non_adj_sum([2, 4, 6, 2, 5]))
def max_sub_arr(arr, k):
    """
    Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum
    values of each sub array of length k.

    For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    10 = max(10, 5, 2)
    7 = max(5, 2, 7)
    8 = max(2, 7, 8)
    8 = max(7, 8, 7)

    Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store
    the results. You can simply print them out as you compute them.
    """
    length = len(arr)
    if k < 1 or k > len(arr):
        return "Wrong k"

    for i in range((length - k) + 1):
        yield max(arr[i:k + i])


# The above code is naive and takes O(n*k) time
# One thing I noticed with this code is we are asked to get sub arrays sequentially. That is, from index 0 to the end.
print(list(max_sub_arr([10, 5, 2, 7, 8, 7], 3)))

def prod_arr(arr):
    """
    Given an array of integers, return a new array such that each element at index i of the new array is the
    product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
    """
    new_arr = []
    for i in range(len(arr)):
        prod = 1
        for j in range(len(arr)):
            if i != j:
                prod *= arr[j]
        new_arr.append(prod)

    return new_arr


print(prod_arr([1, 2, 3, 4, 5]))
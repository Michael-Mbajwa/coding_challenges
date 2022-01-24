def prod_arr(arr):
    """
    Given an array of integers, return a new array such that each element at index i of the new array is the
    product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
    """
    # Initiate the array
    new_arr = [None] * len(arr)

    # Loop through each element in the array
    for i in range(len(arr)):
        prod = 1  # Set product as 1
        # Second looping of the array (This is what makes the code run in O(n)
        for j in range(len(arr)):
            if i != j:  # The index we are on is not part of the multiplication
                prod *= arr[j]
        new_arr[i] = prod
    # This runs in O(n) complexity
    return new_arr


print(prod_arr([1, 2, 3, 4, 5]))
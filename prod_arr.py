import numpy as np


# Third code. Also takes O(n) but does not rely on any external library.
def product_array(arr):
    """
    Given an array of integers, return a new array such that each element at index i of the new array is the
    product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
    """

    # Initialize the prefix products of each item. We will then calculate the products of all the items to the left of i
    prefix_prod = [None] * len(arr)
    i = 0
    while i < len(arr):
        prod = 1
        if arr[0:i]:  # If the array is not empty
            for num in arr[0:i]:
                prod *= num
            prefix_prod[i] = prod
        else:
            prefix_prod[i] = 1
        i += 1

    # Initialize the suffix products of each item. We will calculate the products of all the items to the right of j
    suffix_prod = [None] * len(arr)
    j = 0
    while j < len(arr):
        prod = 1
        if arr[j + 1:]:
            for num in arr[j + 1:]:
                prod *= num
            suffix_prod[j] = prod
        else:
            suffix_prod[j] = 1
        j += 1

    result = [None] * len(arr)
    for i in range(len(arr)):
        result[i] = prefix_prod[i] * suffix_prod[i]

    return result


# Second code I wrote. This takes O(n) time but relies on an external library numpy.
def products(arr):
    """
    Given an array of integers, return a new array such that each element at index i of the new array is the
    product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
    """
    # Initialize the result array
    result = [None] * len(arr)

    for i in range(len(arr)):  # Loop through each item in the array
        prefix = arr[0:i]  # Extract prefix of the item i. Returns an empty list if there no items before it.
        suffix = arr[i + 1:]  # Extract suffix of the item i. Returns an empty list if there no items after it.
        prefix.extend(suffix)  # Combine suffix into prefix
        result[i] = np.prod(prefix)  # Using numpy, multiply all the values and append it in it's right position

    return result


# First code I wrote. This takes O(n^2) time.
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


if __name__ == "__main__":
    print(product_array([1, 2, 3, 4, 5]))
    print(products([1, 2, 3, 4, 5]))
    print(prod_arr([1, 2, 3, 4, 5]))
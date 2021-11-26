def sum_two_numbers_poor(arr, k):
    """
    Given a list of numbers nums and a number k, return whether any two elements from the list add up to k.
    You may not use the same element twice.

    Note: Numbers can be negative or 0.

    Constraints
    n ≤ 100,000 where n is the length of nums
    """
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return True
    return False


def sum_two_numbers_strong(nums, k):
    s = set()
    for i in nums:
        if k-i in s:
            return True
        else:
            s.add(i)
    return None
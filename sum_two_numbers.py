def sum_two_numbers_strong(nums, k):
    """
    Given a list of numbers nums and a number k, return whether any two elements from the list add up to k.
    You may not use the same element twice.
    Note: Numbers can be negative or 0.
    Constraints
    n ≤ 100,000 where n is the length of nums
    """
    if len(nums) > 100000:
        return 'Array too large'

    s = set()
    for i in nums:
        if k-i in s:
            return True
        else:
            s.add(i)
    return None


def two_sum(arr, k):
    if len(arr) > 100000:
        return 'Array too large'

    seen = {}
    for num in arr:
        if k - num in seen:
            return True
        else:
            seen[num] = True
    return False


def sum_two_numbers_naive(arr, k):
    """
    Given a list of numbers nums and a number k, return whether any two elements from the list add up to k.
    You may not use the same element twice.

    Note: Numbers can be negative or 0.

    Constraints
    n ≤ 100,000 where n is the length of nums
    """
    if len(arr) > 100000:
        return 'Array too large'

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return True
    return False

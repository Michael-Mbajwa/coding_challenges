def perm_check(arr):
    """
    A non-empty array A consisting of N integers is given.
    A permutation is a sequence containing each element from 1 to N once, and only once.
    For example, array A such that:
        A[0] = 4
        A[1] = 1
        A[2] = 3
        A[3] = 2
    is a permutation, but array A such that:
        A[0] = 4
        A[1] = 1
        A[2] = 3
    is not a permutation, because value 2 is missing.
    The goal is to check whether array A is a permutation.
    """
    max_arr = max(arr)
    perms = [i for i in range(max_arr + 1) if i > 0]
    if sorted(arr) == perms:
        return 1
    else:
        return 0
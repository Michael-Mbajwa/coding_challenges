def passing_cars(arr):
    """
    A non-empty array A consisting of N integers is given. The consecutive elements of array A represent
    consecutive cars on a road.
    Array A contains only 0s and/or 1s:
        0 represents a car traveling east,
        1 represents a car traveling west.
    The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when
    P is traveling to the east and Q is traveling to the west.
    For example, consider array A such that:
        A[0] = 0
        A[1] = 1
        A[2] = 0
        A[3] = 1
        A[4] = 1
    We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
    """
    if len(arr) <= 1000000000:
        result = []
        zero_index = [index for index, value in enumerate(arr) if value == 0]
        one_index = [index for index, value in enumerate(arr) if value == 1]

        for p in zero_index:
            for z in one_index:
                if p < z:
                    result.append((p, z))

        return len(result)
    return 'Not within range'


print(passing_cars([0, 1, 0, 1, 1]))
def climb_stairs(n, x):
    """
    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a
    function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
    For example, if N is 4, then there are 5 unique ways:
    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of
    positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    """
    if x == 1:
        return 1
    steps = set()
    factors = [i for i in range(1, x+1)]
    arr = [1] * n
    for i in range(len(arr)):
        start_point = sum([arr[i] for i in range(i+1)])
        if start_point <= x:
            for j in factors:
                check_n = start_point
                step_str = str(check_n)
                temp_j = j

                while check_n < n:
                    temp_ch = check_n
                    check_n += temp_j

                    if check_n > n:
                        check_n = temp_ch
                        temp_j -= 1
                    else:
                        step_str += str(temp_j)

                steps.add(step_str)
                steps.add(step_str[::-1])

    return steps  # I choose to return the steps so the result can be easily understood.


print(climb_stairs(5, 3))
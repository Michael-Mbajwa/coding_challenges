def min_rooms(arr):
    """
    Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the
    minimum number of rooms required.

    For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
    :param arr:
    :return:
    """
    schedule = sorted(arr)
    print(schedule)
    rooms = 0
    for i in range(len(schedule)):
        vacancy = 0
        if i == 0:
            pass
        else:
            j = i - 1
            while j >= 0:
                if schedule[i][0] > schedule[j][1]:
                    vacancy += 1
                else:
                    vacancy += 0
                j -= 1
        if vacancy == 0:
            rooms += 1
    return rooms


print(min_rooms([(0, 30), (5, 25), (30, 40), (35, 50), (60, 100), (110, 200), (20, 60)]))
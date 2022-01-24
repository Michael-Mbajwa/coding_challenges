def smallest_window(arr):
    """
    Given an array of integers that are out of order, determine the bounds of the smallest window that must be sorted
    in order for the entire array to be sorted. For example, given [3, 7, 5, 6, 9],you should return(1, 3).
    :param arr:
    :return:
    """
    # Find max bound position
    max_val = arr[0]
    max_pos = None  # The code returns None if there's no sorting to be done
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        elif arr[i] < max_val:
            max_pos = i

    # Find min bound position
    min_val = arr[-1]  # By contradiction, I assume the last item is the minimum number
    min_pos = None  # The code returns None if there's no sorting to be done
    for j in range(len(arr)-2, -1, -1):  # Start looping from behind
        if arr[j] < min_val:  # If the current item is less than the min_val, we update the min_val
            min_val = arr[j]
        else:
            # If the current item is greater than the minimum value, it automatically means some sorting has to be done
            min_pos = j

    return min_pos, max_pos


if __name__ == "__main__":
    print(smallest_window([1, 7, 10, 8, 6, 3, 11, 12]))
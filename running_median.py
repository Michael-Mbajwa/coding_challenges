def running_median(arr):
    """
    This problem was asked by Microsoft.

    Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of
    the list so far on each new element.

    Recall that the median of an even-numbered list is the average of the two middle numbers.

    For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
    2
    1.5
    2
    3.5
    2
    2
    2
    :param arr: array for finding running median.
    :return:
    """
    result = []
    for i in range(len(arr)):
        if i == 0:
            result.append(arr[i])
        else:
            if (len(arr[:(i+1)]) % 2) == 0:
                temp = sorted(arr[:i+1])
                j = len(temp)//2
                x = temp[j]
                y = temp[(j-1)]
                result.append((x+y)/2)
            else:
                temp = sorted(arr[:(i+1)])
                j = len(temp) // 2
                result.append(temp[j])
    return result


if __name__ == "__main__":
    result = running_median([2, 1, 5, 7, 2, 0, 5])
    for i in result:
        print(i)

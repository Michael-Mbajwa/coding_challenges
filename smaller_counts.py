def smaller_counts_right_naive(arr):
    """
    Given an array of integers, return a new array where each element in the new array is the number of smaller elements
    to the right of that element in the original input array.
    For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0] since:
    • There is 1 smaller element to the right of 3
    • There is 1 smaller element to the right of 4
    • There are 2 smaller elements to the right of 9 • There is 1 smaller element to the right of 6
    • There are no smaller elements to the right of 1
    :param arr:
    :return:
    """
    result = [None] * len(arr)
    for i in range(len(arr)):
        if i == len(arr) - 1:
            result[i] = 0
        else:
            temp = arr[i+1:]
            count = 0
            for item in temp:
                if item < arr[i]:
                    count += 1
            result[i] = count

    return result


if __name__ == "__main__":
    print(smaller_counts_right_naive([3, 4, 9, 6, 1]))
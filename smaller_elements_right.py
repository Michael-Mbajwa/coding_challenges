def smaller_elements_right_naive(int_array):
    """
    This problem was asked by Google.

    Given an array of integers, return a new array where each element in the new array is the number of smaller elements
     to the right of that element in the original input array.

    For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

    There is 1 smaller element to the right of 3
    There is 1 smaller element to the right of 4
    There are 2 smaller elements to the right of 9
    There is 1 smaller element to the right of 6
    There are no smaller elements to the right of 1

    :return:
    """
    array_length = len(int_array)
    result = [0] * array_length
    for i in range(array_length-1):
        count = 0
        for num in int_array[i+1:]:
            if num < int_array[i]:
                count += 1

        result[i] = count

    return result


if __name__ == "__main__":
    test_result = smaller_elements_right_naive([3, 4, 9, 6, 1])
    print(test_result)
def reach_last(int_list):
    """
    This problem was asked by Pinterest.

    Given an integer list where each number represents the number of hops you can make, determine whether you can
    reach to the last index starting at index 0.

    For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
    :return:
    """
    last_index = len(int_list) - 1
    total = 0
    for i in range(0, last_index):
        total += int_list[i]

    if total == last_index:
        return True
    return False


if __name__ == "__main__":
    test_result = reach_last([5, 0, 0, 0, 0, 1])
    print(test_result)
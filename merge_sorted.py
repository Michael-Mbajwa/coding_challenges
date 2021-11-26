def merge_sorted(arr):
    """
    Return a new sorted merged list from K sorted lists, each with size N.
    For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]], the result should be
    [10, 12, 15, 15, 17, 20, 20, 30, 32].
    """
    # Naive solution
    merged_list = list()
    for inn_arr in arr:
        for i in inn_arr:
            merged_list.append(i)

    return sorted(merged_list)


print(merge_sorted([[10, 15, 30], [12, 15, 20], [17, 20, 32]]))
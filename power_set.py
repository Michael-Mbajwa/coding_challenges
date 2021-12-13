def power_set(g):
    """
    The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

    For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
    :return:
    """
    arr = list(g)
    final = arr[-1]
    result = [[]]
    for i in range(len(arr)):
        result.append([arr[i]])
        for j in range(i+1, len(arr)):
            root = [arr[i], arr[j]]
            stack = []
            if final not in root:
                stack.append(root)
                while stack:
                    lst = stack.pop()
                    result.append(lst[:])
                    if final not in lst:
                        k = arr.index(lst[-1]) + 1
                        while k < len(arr):
                            stack.append(lst + [arr[k]])
                            k += 1
            else:
                result.append(root)

    return result


if __name__ == "__main__":
   g = {1, 2, 3}
   for subset in power_set(g):
       print(subset)
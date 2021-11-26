def reverse_list(s):
    """My own version of a function that reverses a list of n integers,
    so that the numbers are listed in the opposite order than they were before"""
    n = len(s)
    reversed_list = []
    for i in range(-1, -(n + 1), -1):
        item = s[i]
        reversed_list.append(item)
    return reversed_list


print(reverse_list([4, 6, 3, 9, 0]))
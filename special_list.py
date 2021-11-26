def special_list():
    """A function that produces a list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] that follows this sequence"""
    x = eval(input('Enter an integer that indicates the length of required list: '))
    unique_list = []
    for i in range(1, x + 1):
        value = sum(y for y in range(i))
        list_value = 2 * value
        unique_list.append(list_value)

    return unique_list


print(special_list())
def double_value():
    """Demonstrating how to use Python’s list comprehension syntax to produce
    the list [1, 2, 4, 8, 16, 32, 64, 128, 256]."""
    value = eval(input('Present any integer value: '))
    list_double_value = [1]
    for number in range(1, value):
        value_doubled = list_double_value[-1] * 2
        list_double_value.append(value_doubled)

    return list_double_value


print(double_value())
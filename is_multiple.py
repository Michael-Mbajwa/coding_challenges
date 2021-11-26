def is_multiple(a, b):
    """A function that calculates multiples"""
    if a % b == 0:
        return "Yes"
    else:
        return "No"


print(is_multiple(10, 2))
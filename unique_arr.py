def unique_arr(s):
    """My own version of a function that takes a sequence of numbers and
    determines if all the numbers are different from each other (that is, they are distinct)."""
    n = len(s)
    condition = True
    for i in range(n):
        value_i = s[i]
        for j in range(n):
            if i != j:
                value_j = s[j]
                if value_i == value_j:
                    condition = False
    if not condition:
        return "Duplicates exists"
    else:
        return "No duplicates"


print(unique_arr([1, 2, 3, 3]))
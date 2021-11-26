def two_divisible():
    """A Python program that can take a positive integer greater than 2 as input and write out the
    number of times one must repeatedly divide this number by 2 before getting a value less than 2"""
    number = eval(input('Please provide an integer grater than 2: '))
    count = 0
    if number > 2:
        remainder = number / 2
        count += 1
        while remainder >= 2:
            remainder = remainder // 2
            count += 1
        return count
    else:
        result = "Not greater than 2"
    return result


print(two_divisible())
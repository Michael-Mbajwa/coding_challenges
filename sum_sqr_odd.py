def sum_sqr_odd():
    """A short Python function that takes a positive integer n and
    returns the sum of the squares of all the odd positive integers smaller than n."""
    n = eval(input('Please input a positive integer: '))
    y = str(n)

    if n <= 0:
        print('Sorry, I cannot work with this value.')
    else:
        values = []
        n -= 1
        while n > 0:
            if n % 2 != 0:
                values.append(n)
            n -= 1
        print('Odd values less than {0} are {1}'.format(y, values))
        sum_of_squares = sum((value ** 2) for value in values)
        return sum_of_squares


print(sum_sqr_odd())
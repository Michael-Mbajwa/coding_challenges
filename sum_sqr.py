def sum_sqr():
    """ A short Python function that takes a positive integer n and
    returns the sum of the squares of all the positive integers smaller than n."""
    n = eval(input('Please input a positive integer: '))
    y = str(n)

    if n <= 0:
        print('Sorry, I cannot work with this value.')
    else:
        values = []
        while n > 0:
            n -= 1
            values.append(n)
        print('Values less than {0} are {1}'.format(y, values))
        sum_of_squares = sum((value ** 2) for value in values)
        return sum_of_squares

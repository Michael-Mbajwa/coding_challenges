def check_sum(value):
    """
    I was asked this in an interiew with JP Morgan Chase
    When given a number, this function doubles every second digit of the number from the right and adds everything
    together. If a doubled number results in a number with more than 1 value, you treat each of those numbers separately
    For example, given 1496
    :param value:
    :return:
    """
    num_str = [i for i in str(value)]
    n = len(num_str) - 2
    while n >= 0:
        num = int(num_str[n])

        num = num + num

        if len(str(num)) == 2:
            x = [j for j in str(num)]

            a = x[0]
            b = x[1]
            alpha_ab = int(a) + int(b)
            num_str[n] = alpha_ab
        else:
            num_str[n] = num
        n = n - 2

    main_sum = 0
    for i in num_str:
        try:
            main_sum += int(i)
        except TypeError:
            pass
    return main_sum
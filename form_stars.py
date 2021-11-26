# Collects a number from the user and forms stars with it. For example if 3 is passed, it will produce:
# *
# **
# ***
# **
# *


def form_stars():
    n = eval(input('Provide a number: '))
    star = '*'
    for i in range(1, n + 1):
        print(star * i)
    for j in range(n - 1, 0, -1):
        print(star * j)


form_stars()
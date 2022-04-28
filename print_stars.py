def stars(n):
    """
    Asked by Amazon
    """
    nrows = n * 2 - 1
    star = "*"
    n_steps = 1
    while n_steps < nrows:
        total_space = nrows - n_steps
        space_left = total_space//2
        space_right = space_left
        print(" " * space_left + star * n_steps + " " * space_right)
        n_steps += 2


stars(10)
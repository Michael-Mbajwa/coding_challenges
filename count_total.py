def prefix_sums(arr):
    p = [0] * len(arr)
    for i in range(len(arr)):
        if i == 0:
            p[i] = arr[i]
        else:
            p[i] = p[i - 1] + arr[i]
    return p


def count_total(a, x, y):
    p = prefix_sums(a)
    if x == 0:
        return p[y]
    else:
        return p[y] - p[x - 1]

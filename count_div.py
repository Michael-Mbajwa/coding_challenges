def count_div(a, b, k):
    """
    Write a function:
    def solution(A, B, K)
    that, given three integers A, B and K, returns the number of integers within the range [A..B]
    that are divisible by K, i.e.:
    { i : A ≤ i ≤ B, i mod K = 0 }
    For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers
    divisible by 2 within the range [6..11], namely 6, 8 and 10.
    Write an efficient algorithm for the following assumptions:
        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.
    """
    if a < b and b - a < 2000000001 and k in range(1, 2000000001):
        count = 0
        for i in range(a, b + 1):
            if i % k == 0:
                count += 1

        return count

    return 'Doesn\'t satisfy function constraints.'


print(count_div(5, 25, 3))
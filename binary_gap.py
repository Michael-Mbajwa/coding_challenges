def binary_gap(n):
    """
    A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at
    both ends in the binary representation of N. For example, number 9 has binary representation 1001 and contains
    a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps:
    one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap
    of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary
    representation 100000 and has no binary gaps.
    Write a function:
    def solution(N) that, given a positive integer N, returns the length of its longest binary gap.
    The function should return 0 if N doesn't contain a binary gap.
    For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and
    so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary
    representation '100000' and thus no binary gaps.
    Write an efficient algorithm for the following assumptions: N is an integer within the range [1..2,147,483,647].
    """
    if n in range(1, 2147483648):
        if n < 0:
            return

        val = format(n, 'b')
        print(val)

        if len(val) <= 2:
            return 0

        gaps = []

        for i in range(1, len(val) - 1):
            if val[i - 1] == '1' and val[i] == '0':
                count = 1
                while (count + i) < (len(val) - 1) and val[count + i] == '0':
                    count += 1
                if count + i < len(val) and val[count + i] == '1':
                    gaps.append(count)
            else:
                gaps.append(0)

        return max(gaps)

    return 'Not within range'


print(binary_gap(5))
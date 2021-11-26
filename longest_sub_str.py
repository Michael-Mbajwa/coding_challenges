def longest_sub_str(s, k):
    """
    Given an integer k and a string s, find the length of the longest substring that contains at most k
    distinct characters.

    For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
    :return:
    """
    if len(s) == 1:
        return 1

    paths = []
    len_paths = []
    for i in range(len(s)):
        j = i + 1
        count = 0
        cons = {s[i]}
        path = s[i]
        log = True
        while j < len(s) and log:
            cons.add(s[j])
            count += 1
            path += s[j]
            j += 1
            if len(cons) > k:
                path = path[:len(path) - 1]
                count = count - 1
                log = False

        paths.append(path)
        len_paths.append(count)

    return paths, len_paths  # I choose to return a list of the path so it can be easily understood. Not advisable
    # for interview.


print(longest_sub_str('abcbdd', 5))
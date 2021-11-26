def auto_com(s, s_s):
    """
    Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
    return all strings in the set that have s as a prefix.

    For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

    Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries."""

    """
    - The best data structure for faster searching of string is TRIE.
    Tries are an extremely special and useful data-structure that are based on the prefix of a string. 
    - They are used to represent the “Retrieval” of data.
    A Trie is a special data structure used to store strings that can be visualized like a graph. 
    It consists of nodes and edges.
    Each node consists of at max 26 children and edges connect each parent node to its children. 
    These 26 pointers are nothing but pointers for each of the 26 letters of the English alphabet
    A separate edge is maintained for every edge.
    Strings are stored in a top to bottom manner on the basis of their prefix in a trie.
    All prefixes of length 1 are stored at until level 1, all prefixes of length 2 are sorted at until 
    level 2 and so on.
    """
    s_l = len(s)
    result = set()
    for i in s_s:
        if i[0:s_l] == s:
            result.add(i)
    return result
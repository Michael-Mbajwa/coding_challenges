def balanced_brackets(par):
    """
    Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced
    (well-formed).

    For example, given the string "([])[]({})", you should return true.

    Given the string "([)]" or "((()", you should return false.
    :return:
    """
    # Basic check
    if len(par) % 2 != 0:
        return False
    stack = []
    i = 0
    balanced = True
    while i < len(par) and balanced:
        symbol = par[i]
        if symbol in '([{':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                balanced = False
            else:
                symbol2 = stack.pop(-1)
                if not matches(symbol2, symbol):
                    balanced = False
        i += 1

    if balanced and len(stack) == 0:
        return True
    else:
        return False


def matches(op, cl):
    open = '([{'
    close = ')]}'
    return open.index(op) == close.index(cl)



def balanced_brackets(par):
    """
    Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced
    (well-formed).

    For example, given the string "([])[]({})", you should return true.

    Given the string "([)]" or "((()", you should return false.
    :return:
    """
    # Basic check
    if len(par) % 2 != 0:  # If the brackets are not even then it means we already know they are imbalanced
        return False

    stack = []
    i = 0
    balanced = True  # Initial assumption that is balanced
    while i < len(par) and balanced:
        symbol = par[i]
        if symbol in '([{':
            stack.append(symbol)  # We only append opening brackets
        else:  # If we encounter a closing bracket
            if len(stack) == 0:
                balanced = False  # If there is no item in the stack, it means there's no matching opening bracket.
            else:  # So there is an item in the stack. We can pop it and check if it matches
                symbol2 = stack.pop(-1)
                if not matches(symbol2, symbol):  # Function checks if the match, if it doesn't, it is not balanced
                    balanced = False
        i += 1

    if balanced and len(stack) == 0:  # At the end of the loop and we are still balanced and the stack is empty, our
        # par is balanced
        return True
    else:
        return False


def matches(op, cl):
    open = '([{'
    close = ')]}'
    return open.index(op) == close.index(cl)



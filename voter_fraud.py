def voter_fraud(arr_2d):
    """
    Given a two dimensional list of integers votes, where each list has two elements [candidate_id, voter_id],
    report whether any voter has voted more than once.
    Constraints:
    votes = [
    [3, 1],
    [3, 0],
    [3, 4],
    [3, 3],
    [3, 2]]. Result = False
    n ≤ 100,000 where n is the length of votes
    """
    test = set()
    for arr in arr_2d:
        if arr[1] in test:
            return True
        else:
            test.add(arr[1])
    return False
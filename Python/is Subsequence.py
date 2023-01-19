def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    positions = []
    for element in s:
        if element not in t:
            return False
        else:
            positions.append(t.index(element))
    positions_copy = positions[:]
    if positions == positions_copy:
        return True
    return False
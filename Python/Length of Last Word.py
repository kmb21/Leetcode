def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    q = s.split()
    last_word = q[len(q)-1]
    return len(last_word)
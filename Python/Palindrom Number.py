def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    if x[:len(x)] == x[::-1]:
        return True
    return False
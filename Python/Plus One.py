def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    l = []
    string = ""
    for integer in digits:
        string += str(integer)
    sum = int(string)+1
    sum = str(sum)
    n = 1
    q = 0
    while n <= len(sum):
        l.append(sum[q:n])
        n += 1
        q += 1
    return l
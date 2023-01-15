def getNoZeroIntegers(n):
    """
    :type n: int
    :rtype: List[int]
    """
    for item in range(n):
        for number in range(n):
            if '0' not in str(number) and '0' not in str(item):
                sum = item + number
                if sum == n:
                    if item > number:
                        return [item, number]
                    else:
                        return [number, item]
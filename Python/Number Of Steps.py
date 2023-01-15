def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    num_steps = 0
    while num != 0:
        if num%2 == 0:
            num = num / 2
            num_steps += 1
        else:
            num -= 1
            num_steps += 1

    return num_steps
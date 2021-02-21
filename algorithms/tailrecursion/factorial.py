def factorial(num, result = 1):
    '''
    Returns the factorial of a number.
    '''
    if num <= 1:
        return result

    result = result * num
    num -= 1
    return factorial(num, result)

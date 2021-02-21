def factorial(num):
    '''
    Returns the factorial of a number.
    '''
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

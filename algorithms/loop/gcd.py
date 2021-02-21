def euclidean(a, b):
    '''
    Returns the Greatest Common Division of 2 numbers.

    Uses the Euclidean algorithm to calculate the GCD.
    '''
    if b > a:
        a, b = b, a

    while a % b > 0:
        a, b = b, a % b
    return b

def factorization(a, b):
    '''
    Returns the Greatest Common Division of 2 numbers.

    Uses factorization to calculate the GCD.
    '''
    if b > a:
        a, b = b, a

    divisors = []
    for n in range(1, b + 1):
        if a % n == 0 and b % n == 0:
            divisors.append(n)
            a = a / n
            b = b / n
    result = 1
    for d in divisors:
        result *= d
    return result

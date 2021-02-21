def euclidean(a, b):
    '''
    Returns the Greatest Common Division of 2 numbers.

    Uses the Euclidean algorithm to calculate the GCD.
    '''
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b

    return euclidean(b, a % b)

def factorization(a, b, n=2, result=1):
    '''
    Returns the Greatest Common Division of 2 numbers.

    Uses factorization to calculate the GCD.
    '''
    if b > a:
        a, b = b, a

    if a == 1 and b == 1:
        return result

    divided = False
    if a % n == 0 and b % n == 0:
        result *= n

    if a % n == 0:
        a = a / n
        divided = True

    if b % n == 0:
        b = b / n
        divided = True

    if not divided:
        n += 1
    return factorization(a, b, n, result)

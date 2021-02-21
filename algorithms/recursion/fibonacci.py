def fibonacci(nth):
    '''
    Return the nth number in the Fibonacci sequence.

    The Fibonacci sequence starts with 1 1 2 3 5 8.
    For instance, for nth 5 it returns 8.
    '''
    if nth == 0:
        return 1

    if nth == 1:
        return 1

    return fibonacci(nth - 1) + fibonacci(nth - 2)

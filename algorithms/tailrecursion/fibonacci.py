def fibonacci(nth, prev=1, curr=1):
    '''
    Return the nth number in the Fibonacci sequence.

    The Fibonacci sequence starts with 1 1 2 3 5 8.
    For instance, for nth 5 it returns 8.
    '''
    if nth == 0:
        return curr

    if nth == 1:
        return curr

    prev, curr = curr, prev + curr
    nth -= 1
    return fibonacci(nth, prev, curr)

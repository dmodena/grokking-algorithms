def sum(arr):
    '''
    Returns the sum of all elements in an array.
    '''
    if len(arr) > 0:
        return arr.pop(0) + sum(arr)
    return 0

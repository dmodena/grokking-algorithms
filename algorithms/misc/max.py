def max(arr):
    '''
    Returns the hightest value in the array.
    '''
    replica = arr.copy()
    replica.sort()
    return replica.pop()

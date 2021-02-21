def max(arr):
    '''
    Returns the hightest value in the array.
    '''
    result = arr[0]
    for n in arr:
        if n > result:
            result = n
    return result

def sum(arr, result = 0):
    '''
    Returns the sum of all elements in an array.
    '''
    if len(arr) == 0:
        return result

    result += arr.pop(0)
    return sum(arr, result)

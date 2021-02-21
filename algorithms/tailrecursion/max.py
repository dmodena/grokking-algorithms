def max(arr, result=-float('inf')):
    '''
    Returns the hightest value in the array.
    '''
    if len(arr) == 0:
        return result

    num = arr.pop()
    if num > result:
        result = num
    return max(arr, result)

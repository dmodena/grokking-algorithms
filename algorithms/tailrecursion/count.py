def count(arr, result=0):
    '''
    Counts the number of elements in an array.
    '''
    if len(arr) == 0:
        return result

    arr.pop()
    result += 1
    return count(arr, result)

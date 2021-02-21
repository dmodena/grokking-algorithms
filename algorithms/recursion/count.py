def count(arr):
    '''
    Counts the number of elements in an array.
    '''
    if len(arr) == 0:
        return 0

    arr.pop()
    return 1 + count(arr)

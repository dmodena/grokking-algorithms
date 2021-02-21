def max(arr):
    '''
    Returns the hightest value in the array.
    '''
    if len(arr) == 1:
        return arr[0]

    if arr[1] > arr[0]:
        arr.pop(0)
    else:
        arr.pop(1)

    return max(arr)

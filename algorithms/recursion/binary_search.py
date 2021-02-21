def binary_search(arr, item):
    '''
    Runs a binary search, returning the item if found.

    Items must be comparable and arr must be in ascending order.
    '''
    if len(arr) == 0:
        return None

    if len(arr) == 1:
        if arr[0] == item:
            return arr[0]
        return None

    guess_idx = len(arr) // 2
    if arr[guess_idx] == item:
        return item

    if arr[guess_idx] > item:
        arr = arr[:guess_idx]
    elif arr[guess_idx] < item:
        arr = arr[guess_idx + 1:]

    return binary_search(arr, item)

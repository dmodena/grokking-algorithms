def binary_search(arr, item):
    '''
    Runs a binary search, returning the item if found.

    Items must be comparable and arr must be in ascending order.
    '''
    min_idx = 0
    max_idx = len(arr) - 1
    while min_idx <= max_idx:
        guess_idx = (min_idx + max_idx) // 2
        if arr[guess_idx] == item:
            return arr[guess_idx]

        if arr[guess_idx] > item:
            max_idx = guess_idx - 1
        elif arr[guess_idx] < item:
            min_idx = guess_idx + 1

    return None

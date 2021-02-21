def select_sort(arr):
    '''
    Returns ordered arr using select sort.
    '''
    new_arr = []
    for i in range(len(arr)):
        lowest_idx = get_lowest_index(arr)
        new_arr.append(arr.pop(lowest_idx))
    return new_arr

def get_lowest_index(arr):
    '''
    Returns index of lowest item in array.
    '''
    if len(arr) == 0:
        return None

    lowest_idx = 0
    for idx in range(1, len(arr)):
        if arr[idx] < arr[lowest_idx]:
            lowest_idx = idx
    return lowest_idx

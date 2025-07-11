def recursive_binary_search(arr, target, start_index, end_index):
    if start_index > end_index:
        return -1
    mid = (start_index + end_index) // 2
    mid_val = arr[mid]
    if mid_val == target:
        return mid
    elif mid_val < target:
        return recursive_binary_search(arr, target, mid + 1, end_index)
    else: return recursive_binary_search(arr, target, start_index, mid - 1)
array=[11,22,33,44,55,66]
print(recursive_binary_search(array,11,0,5))
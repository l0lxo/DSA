def binary_search(arr, key_value):
    start = 0
    end = len(arr) - 1

    while start <= end :
        mid = (start + end) // 2
        mid_val = arr[mid]
        if mid_val == key_value:
            return mid_val
        elif key_value < mid_val:
            start = 0
            end = mid-1
        elif key_value > mid_val:
            start = mid + 1
            end = end -1
    return -1

print(binary_search([1,2,3,4,5],1))
def binary_search_recursive(ls, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if ls[mid] == target:
        return mid
    elif ls[mid] > target:
        return binary_search_recursive(ls, target, low, mid - 1)
    else:
        return binary_search_recursive(ls, target, mid + 1, high)

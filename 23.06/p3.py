def is_sorted(arr):
    if not arr:
        return False
    
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
        
    return True


print(is_sorted([1,2,3]))
print(is_sorted([1]))
print(is_sorted([]))
print(is_sorted([1,5,2]))
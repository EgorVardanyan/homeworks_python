

    
def bin(lst, target):
    start = 0
    end = len(lst) - 1
    while start < end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            start = mid + 1
        else: 
            end = mid - 1
    return -1

print(bin([1,2,3,4,5,6,7],6))

        

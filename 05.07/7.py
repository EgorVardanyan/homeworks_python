def insertion_sort(ls: list) -> list:
    size = len(ls)
    for i in range(1, size):
        key = ls[i]
        j = i - 1
        while j >= 0 and key < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls


ls = [83, 21, -3, 245, 4]
print(insertion_sort(ls))

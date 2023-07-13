def bubble_sort(ls):
    size = len(ls)

    for i in range(size - 1):
        flag = False
        for j in range(0, size - i - 1):
            if ls[j] > ls[j + 1]:
                flag = True
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
        if not flag:
            break
    return ls


ls = [45, 11, 43, 6, 12, -1, 341]
print(bubble_sort(ls))


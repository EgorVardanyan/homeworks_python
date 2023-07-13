def selection_sort(ls):
    size = len(ls)
    for i in range(size):
        min_i = i
        for j in range(i + 1, size):
            if ls[j] < ls[min_i]:
                min_i = j
        ls[i], ls[min_i] = ls[min_i], ls[i]
    return ls


ls = [83, 21, -3, 245, 4]
print(selection_sort(ls))

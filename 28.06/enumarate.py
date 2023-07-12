def en(iter, start = 0):
    if start > len(iter):
        return "sxal"
    count = start
    for i in iter:
        yield(count,i)
        count += 1
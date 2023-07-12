def filter(function, iterable):
    result = []

    if function is None:
        for i in iterable:
            if i:
                result.append(i)
    else:
        for j in iterable:
            if function(j):
                result.append(j)

    return result

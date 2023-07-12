def map(x, iterable):
    result = []
    for i in iterable:
        result.append(x(i))
    return result
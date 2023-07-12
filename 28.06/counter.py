def counter(count):
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

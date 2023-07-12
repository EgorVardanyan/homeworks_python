def zip(*iterables):
    iters = [iter(i) for i in iterables]

    while True:
        try:
            result = [next(i) for i in iters]
            yield tuple(result)

        except StopIteration:
            return
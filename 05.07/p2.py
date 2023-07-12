def fibonacci_nth(x: int) -> int:
    if x in (1, 2):
        return x - 1

    return fibonacci_nth(x - 1) + fibonacci_nth(x - 2)

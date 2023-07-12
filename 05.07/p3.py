def sum_digits(x: int) -> int:
    if x < 10:
        return x

    return (x % 10) + sum_digits(x // 10)


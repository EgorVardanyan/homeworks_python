n = int(input("Enter the number:"))
def print_pattern(n):
    i = 1
    while i <= n:
        print(*[j for j in range(1, i + 1)], sep=' ')
        i += 1


print_pattern(n)

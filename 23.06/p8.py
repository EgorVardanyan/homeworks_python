def power_of(n):
    def power(x):
        return pow(x, n)
    
    return power


foo = power_of(5)

print(foo(2))
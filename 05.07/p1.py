def cache_fact():
    table = {0:1}
    def fact(n):
        if n in table:
            return table[n]
        else:
            table[n] = n * fact(n - 1)
            return table[n]
        
    return fact

f = cache_fact()


def outer_function(x):
    def inner_function(factor):
        return x * factor
    
    return inner_function


print(outer_function(5)(10))
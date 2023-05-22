from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    #checks if the input is an integer
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be a postive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    
for n in range(1, 501):
    # print(n, ';', fibonacci(n))
    print(fibonacci(n+1) / fibonacci(n))

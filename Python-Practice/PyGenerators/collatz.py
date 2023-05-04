def collatz(n):
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n
        if n == 1:
            break

def example_collatz():
    n = 27
    seq = list(collatz(n))
    print(seq)

example_collatz()
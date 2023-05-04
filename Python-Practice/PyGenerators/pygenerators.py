#a generator is a regular function but with yield
def get_values():
    yield "hello"
    yield "world"
    yield 123
    return 42

def example_get_values():
    # gen = get_values()
    #callinga genrrator doesn't actually do anything so you have to use 'next
    for x in get_values():
        print(x)

example_get_values()

#most common use of generators is to define an iterator of a class

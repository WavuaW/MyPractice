def example_gen_comp():
    #this is a list comprehension
    squares = [x*x for x in range(5)]
    #if your generator is simple enough you can define it as a ;list comprehension and replace [] with ()
    square = (x*x for x in range(5))

    print(next(square))

example_gen_comp()
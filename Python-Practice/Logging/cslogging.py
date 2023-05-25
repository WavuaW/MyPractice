def add(x, y):
    return x + y 

def subrtact(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x , y):
    return x / y

num_1 = 10
num_2 = 5

add_result = add(num_1, num_1)
print('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subrtact(num_1, num_2)
print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
print('Div: {} + {} = {}'.format(num_1, num_2, div_result))

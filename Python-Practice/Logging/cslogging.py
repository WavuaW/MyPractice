import logging
import employeeclass

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def add(x, y):
    return x + y 

def subrtact(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x , y):
    return x / y

num_1 = 20
num_2 = 10

add_result = add(num_1, num_1)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subrtact(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} + {} = {}'.format(num_1, num_2, div_result))

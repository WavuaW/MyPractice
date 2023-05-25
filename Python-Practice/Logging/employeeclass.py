import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('employee.log')

logger.addHandler(file_handler)

logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

class Employee:
    """A simple employee class"""

    def __init__(self, first, last):
        self.first = first 
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Chris', 'Wavua')
emp_3 = Employee('Jane', 'Doe')
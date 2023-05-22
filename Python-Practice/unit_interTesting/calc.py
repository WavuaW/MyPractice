def add(self, x, y):
    """Adds two numbers"""
    return x + y

def subtract(self, x, y):
    """Subtracts one number from another"""
    return x - y

def multiply(self, x, y):
    """Multiplies two numbers"""
    return x * y

def divide(self, x, y):
    """Divides one number by another"""
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")
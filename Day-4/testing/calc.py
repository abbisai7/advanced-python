def add(a,b):
    """ADD"""
    return a+b

def divide(a,b):
    if b == 0:
        raise ValueError("Cant divide by zero")
    return a/b
def add(a,b):
    return a+b

def div(a,b):
    if b==0:
        raise ZeroDivisionError('b cannot be zero')
    return a/b

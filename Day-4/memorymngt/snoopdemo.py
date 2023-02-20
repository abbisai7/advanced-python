import snoop
#pip install snoop 
'''
snoop is a Python package that prints the lines of code being 
executed along 
with the values of each variable by adding only one decorator.
debugging and understandning line by line behaving 
'''
@snoop
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


print(fib(4))

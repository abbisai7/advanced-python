'''
def say_hello(name):
    return f"Hello {name} !"

def appreciate(name):
    return f'Yo {name}, you are great!!'

def greet(funcptr):
    #logging,cahching,automation
    return funcptr("Sai")
    
print(greet(say_hello))
print(greet(appreciate))
'''

def extra(func):
    def wrapper():
        print("Hi")
        func()
        print("Cool")
    return wrapper

@extra
def invoek():
    print("Sai")
    
invoek()
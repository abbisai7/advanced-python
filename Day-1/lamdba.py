#lambda fucntion for performance

add5 = lambda x:x+5

print(add5(5))

def do_something(func,val):
    ''' do extra work logging,security,security check,profile,cache'''
    return func(val)

myfunc = lambda x:x+1

result = do_something(myfunc,10)

print(result)

info = lambda x : True if x.startswith("S") else False

print(info("Sai"))


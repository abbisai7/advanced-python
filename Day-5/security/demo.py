#exploit of eval and excec are dangerous


def add(a,b):
    return eval("%s+%s"%(a,b))
    
user_input ={
    "a":"__import__('os').system('dir')",
    "b":2,
}

result = add(user_input["a"],user_input["b"])
print("%d" %(result))

#please validate the input before passing

user_password = "admin"

if user_password == input("ENter password"):
    print("Welcome")
else:
    print("incorrect")
    

# string formatting

CONFIG = {
    "API_KEY": "771df488714111d39138eb60df756e6b"
}


class Person(object):
  def __init__(self, name):
    self.name = name


def print_nametag(format_string, person):
  return format_string.format(person=person)


person = Person("Murthy")

greeting = print_nametag("{person.__init__.__globals__[CONFIG][API_KEY]}",person)
print(greeting)

# Output : Hi, my name is Murthy. I am a Person.
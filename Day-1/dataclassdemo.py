'''
Model class - Mapped to table of Database(ORM)

'''

from dataclasses import dataclass

@dataclass
class Car:
    color:str
    mileage:float
    automatic:bool

c1=Car("Grey","25","True")
print(c1.color)
print(c1)


'''


'''
# pip install pympler

from pympler import asizeof
from collections import namedtuple

Point = namedtuple("Point","x y z")
p=Point(10,"yes","20")

namedtuple_size = asizeof.asizeof(p)
dict_size = asizeof.asizeof(p._asdict())


gain = 100 - namedtuple_size / dict_size * 100

print(f'Named Tuple : {namedtuple_size} is bytes : {gain:.2f}% smaller')
print(dict_size)

print(p.x)
print(p[1])
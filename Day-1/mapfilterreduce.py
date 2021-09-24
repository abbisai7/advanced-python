#map,filter,reduce are paradigms of functional programming

#map(func,*iterable) --> processed result

names = ["sai","chaithanya"]

res = list(map(str.upper,names))
print(res)

numbers = [1,2,3,4,5]

squared = list(map(lambda num : num**2 , numbers))

print(squared)
print(type(squared))

def CtoF(C):
    res = 9/5 * C +32
    return res
def FtoC(F):
    res= (F-32) * 5/9

cTemps= [40,50,60,70,80]

fTemps= list(map(CtoF,cTemps))
print(fTemps)

#filter

scores = [33,68,70,67,88]

res1 = list(filter(lambda x: x>75 ,scores))
print(res1)

my_list =[1,4,9,16,25]
new_list = list(filter(lambda x: x%2 ==1,my_list))
print(new_list)


#reduce --> aggregarated single value ex:- total ,sum

from functools import reduce

nums = [3,4,6,9,10]

def custom_sum(first,second):
    return first+second

result = reduce(custom_sum,nums)
print(result)

result = reduce(lambda x,y: x+y ,nums)
print(result)

#realtime
import functools
import os,os.path
import operator

files = os.listdir(os.path.expanduser("."))
res =  functools.reduce(operator.add,map(os.path.getsize,files))
print(res)


import numpy as np

x = np.array([100,200,300,400,500])
sqaurer = lambda x: x**2
squares = np.array([sqaurer(i) for i in x])
print(squares)

vfunc = np.vectorize(sqaurer)
print(vfunc(x))


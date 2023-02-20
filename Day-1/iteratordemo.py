#demand based iteration
#iterable allow us to iter us over a iterable 

nums = [1,2,3,4,5]
it = iter(nums)
print(type(it))
print(it.__next__())
print(next(it))

cubes = (1,8,27,64,125)
cube = iter(cubes)
print(type(cube))
print(next(cube))
print(next(cube))


#custom iterator

class Head:
    def __init__(self,max = 5):
        self.num = 1
        self.max = max
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=self.max:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
        
try:
    values = Head(7)
    print(type(values))
    print(values.__next__())
    for i in values:
        print(i)
except Exception as e:
    print(e)

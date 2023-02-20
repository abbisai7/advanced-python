#generato function are special type of itertators, that iterate only once.
#it doesnt save any value in memory,generates the value on demand by using yield ,fucntion refernece is stored where it is stoped

def square_numbers(nums):
    result = []
    for i in nums:
        return i ** i

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)
print(type(my_nums))

def square_numbers(nums):
    for i in nums:
        yield i * i

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)
print(type(my_nums))
print(my_nums.__next__())
print(my_nums.__next__())
print(my_nums.__next__())
#print(my_nums.__next__())
#print(my_nums.__next__())
#print(my_nums.__next__())

alist = [1,2,3,4,5]
out = [ i*i for i in alist]
print(type(out))

alist = [1,2,3,4,5]
out = ( i*i for i in alist)
print(type(out))
print(next(out))
for i in out:
    print(i)
    
#custom generator

def top_five():
    n = 1
    while n<=5:
        sq = n*n
        yield sq
        n += 1

values = top_five()
for i in values:
    print(i)
    


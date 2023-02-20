#profiling in python = custom decorator

import functools,time

def timeit(func):
    def wrappaer(*args,**kwargs):
        start = time.perf_counter()
        value = func(*args,**kwargs)
        end = time.perf_counter()
        print(f'Time taken {func.__name__} {end-start:.4f}')
        return value
    return wrappaer

@timeit
def task(numTimes):
    for _ in range(numTimes): # throwaway variable
        sum( [i**2 for i in range(10000)])
        
task(1)
task(999)

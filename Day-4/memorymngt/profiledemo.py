import gc
#import memory_profiler

@profile
def my_func():
    a =[1]*(10**6)
    b = [2]*(2*10**7)
    del b 
    gc.collect()
    return a

if __name__ == "__main__":
    my_func()

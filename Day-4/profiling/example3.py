from memory_profiler import profile
#remove del and profile and observe that it uses more memory
# as we are not deallocating 
'''
This kind of unused variables can pile up over time and flood 
memory with unused data which is not 
needed anymore. We can use memory_profiler to find out such code.
'''

@profile(precision=3)
def main_func():
    import random
    arr1 = [random.randint(1, 10) for i in range(100000)]
    arr2 = [random.randint(1, 10) for i in range(100000)]
    arr3 = [arr1[i]+arr2[i] for i in range(100000)]
    tot = sum(arr3)
    print(tot)


if __name__ == "__main__":
    main_func()


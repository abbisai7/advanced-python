from memory_profiler import profile
import gc


@profile
def main_func():
    import random
    arr1 = [random.randint(1, 10) for i in range(100000)]
    arr2 = [random.randint(1, 10) for i in range(100000)]
    arr3 = [arr1[i]+arr2[i] for i in range(100000)]
    del arr1
    del arr2
    tot = sum(arr3)
    del arr3
    gc.collect()
    print(tot)


if __name__ == "__main__":
    main_func()

#python - m memory_profiler example1.py

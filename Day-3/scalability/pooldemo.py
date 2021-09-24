import multiprocessing
import os 

def square(n):
    print("Worker process for {0} is {1}".format(n,os.getpid()))
    return n*n

if __name__ == "__main__":
    my_list = [1,2,3,4,5,9-6,7,8,9,10,11,12]
    p = multiprocessing.Pool()
    
    resullt = p.map(square,my_list)
    print(resullt)
    
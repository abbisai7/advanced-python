import time
import random
import os,psutil,gc

names = ["sai","chai","thanya","boa"]
majors = ["cse","ece","eee","mech"]

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id' : i,
            'name' : random.choice(names),
            'major' : random.choice(majors),
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id' : i,
            'name' : random.choice(names),
            'major' : random.choice(majors),
        }
        yield person


if __name__ == "__main__":
    t1 = time.process_time() #time start
    people = people_list(1000000)
    t2 = time.process_time() #time end
    print("Time taken with list:{} secs".format(t2-t1))
    print("Memmory Usage with list {}".format( psutil.Process(os.getpid()).memory_info()))
    
    import gc
    del people
    gc.collect() # memory clean
    
    t1 = time.process_time() #time start
    people = people_generator(1000000)
    print(next(people))
    t2 = time.process_time() #time end
    print("Time taken with generator:{} secs".format(t2-t1))
    print("Memmory Usage with generator {}" .format(psutil.Process(os.getpid()).memory_info()))
    
    import gc
    del people
    gc.collect() # memory clean
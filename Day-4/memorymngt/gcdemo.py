import gc

def create_cycle(list):
    
    list.append(list)
    
def main():
    print("In main - before garbage refcount {}".format(gc.get_count()))
    print("Crating garbage")
    list = [10,20,30,40]
    for i in range(8):
        create_cycle(list)
    print("In main - after garbage refcount {}".format(gc.get_count()))  
    print("collectiing") 
    n = gc.collect()
    print("unreachable {}".format(n))
    print("Un collectable garbage",gc.garbage)
    print("In main afer garbage refcount is ",gc.get_count())
    
if __name__ == "__main__":
    print("Default threeshold",gc.get_threshold())
    main()
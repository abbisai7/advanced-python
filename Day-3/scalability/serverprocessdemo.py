import multiprocessing

def print_records(records):
    for rec in records:
        print(f"Name {rec[0]} age {rec[1]}")

def insert_records(records,recs):
    recs.append(records)
    print("New Record is stored")

if __name__=="__main__":
    with multiprocessing.Manager() as mngr:
        records = mngr.list([("Murthy",10),("kiran",30)])
        new_record = ("Malika",20)
        
        p1 = multiprocessing.Process(target=insert_records, args=(new_record,records))
        p2 = multiprocessing.Process(target=print_records,args = (records,))
        
        p1.start()
        p1.join()
        p2.start()
        p2.join()
        
        print("Main process is doing something")
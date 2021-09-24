import threading
import datetime

class MyThread(threading.Thread):
    def __init__(self,name,counter):
        threading.Thread.__init__(self)
        self.name=name
        self.counter=counter
        self.threadID=counter
        
    def run(self):
        print("Starting"+self.name)
        threadLock.acquire()
        print_date(self.name,self.counter)
        threadLock.release()
        print("exitinng"+self.name)
        
def print_date(name,counter):
    datefields= []
    data = datetime.date.today()
    datefields.append(data)
    print(f'{name} - {counter} - {datefields[0]}')
        
    
threadLock = threading.Lock()

if __name__ == '__main__':
    thread1=MyThread("exporting",101)
    thread1.start()
    thread2=MyThread("downloading",202)
    thread2.start()
    
    print("Mani thread i also doing something")
    
    thread1.join()
    print("done1")
    thread2.join()
    
    print("done")
    
    
# structural pattern - facade with composition

#ordering.py
class Ordering:
    #sybsystem-1
    def order(self):
        print("Ordering")

#preparing.py
class Preparing:
    #sybsystem-2
    def prepare(self):
        print("Preparing")

#delivering.py
class Delivering:
    #sybsystem-3
    def deliver(self):
        print("Delviering")
        
class Operator():
    #facade
    def __init__(self):
        self.Ordering = Ordering()
        self.Preparing = Preparing()
        self.Delivering = Delivering()
    
    def completeOrder(self):
        self.Ordering.order()
        self.Preparing.prepare()
        self.Delivering.deliver()

if __name__ == "__main__":
    op = Operator()
    op.completeOrder()
    print("Order Completed")
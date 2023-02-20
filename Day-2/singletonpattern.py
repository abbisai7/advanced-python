
class BankSingleTon:
    __instance__ = None
    
    def __init__(self):
        if BankSingleTon.__instance__ is None:
            BankSingleTon.__instance__ = self
        else:
            raise Exception("Instance is already is created")
        
    @staticmethod
    def get_instance():
        if not BankSingleTon.__instance__:
            BankSingleTon()
        return BankSingleTon.__instance__

b = BankSingleTon()
print(b)
c = BankSingleTon.get_instance()
print(c)
#schema, data structure, model, entity , object model, DTO
# for Sqlalchemy ORM  table/datastructure  -crud without sql statements

class Employee:
     def __init__(self,first,last,pay) -> None:
         self.first = first
         self.last = last
         self.pay = pay
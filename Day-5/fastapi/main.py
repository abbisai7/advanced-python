from typing import Optional
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

fast = FastAPI()

@fast.get("/")
def home():
    return {"msg":"welcome to fast api"}

@fast.get("/contacts{cid}")
def contact_details(cid:int,page:Optional[int] =1):
    if page:
        return {"cid ":cid,"page":page}
    return {"contact_id":cid}

#DTO v/s ORM
class Contact(BaseModel):
    cid : int
    fname : str
    lname : str
    username : str
    password : str
 
@fast.post("/contact",description="Create a single contact")   
def create_contact(contact:Contact):
    #add db logic here to insert new contact
    return contact
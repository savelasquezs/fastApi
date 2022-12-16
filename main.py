# python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastApi
from fastapi import FastAPI
from fastapi import Body


app=FastAPI()

#models
class Person(BaseModel):
    firstName:str
    lastName:str
    age: int
    hairColor: Optional[str]="Black"
    isMarried:Optional[bool]=None

@app.get("/")
def home():
    return {"Hello":"World"}

# request and response body
@app.post("/person/new")
def createPerson(person:Person=Body(...)):
    return person
    
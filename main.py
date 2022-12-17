# python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastApi
from fastapi import FastAPI
from fastapi import Body, Query


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

# valiadciones: query parameters
@app.get("/person/detail")
def showPerson(
    name:Optional[str]=Query(None, min_length=1, max_length=50),
    age:str=Query(...)
):
    return {name:age}
    
# python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastApi
from fastapi import FastAPI
from fastapi import Body, Query, Path


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
    name:Optional[str]=Query(
        None,
        min_length=1,
        max_length=50,
        title="Person name",
        description="this is the person description. it is between 1 and 50 characters"
        ),
    age:str=Query(
        ...,
        title="Person Age",
        description="this is the person age. it's required"
        )
):
    return {name:age}
#  validaciones path operations
@app.get("/person/detail/{person_id}")
def showPerson(
    person_id:int=Path(
        ...,
        gt=0,
        title="person_id",
        description="this is the unique person id")
):
    return {person_id:"it exists"}              
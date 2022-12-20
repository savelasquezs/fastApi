# python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastApi
from fastapi import FastAPI
from fastapi import Body, Query, Path


# Validaciones de clases
from pydantic import Field,EmailStr
from enum import Enum

class HairColor(Enum):
    white="White"
    black="Black"
    red="Red"
    blonde="Blonde"



app=FastAPI()

#models
class Location(BaseModel):
    city:str
    state:str
    country:str
    
    class Config:
        schema_extra={
            "example":{
                "city":"Medellín",
                "state":"Antioquia",
                "country":"Colombia",
            }
        }

class Person(BaseModel):
    firstName:str=Field(...,min_length=1,max_length=50)
    lastName:str=Field(...,min_length=1,max_length=50)
    age: int=Field(...,gt=1,le=50)
    hairColor: Optional[HairColor]=Field(default=None)
    isMarried:Optional[bool]=Field(default=None)
    email:EmailStr
    
    class Config:
        schema_extra={
            "example":{
                "firstName":"Santiago",
                "LastName":"velasquez",
                "age":17,
                "haircolor":"blonde",
                "isMarried":True,
                "email":"santyvano@outlook.com"
                
            }
        }

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

# validaciones request body 
@app.put("/person/{person_id}")
def update_person(
    person_id:int=Path(
        ...,
        title="person id",
        description="This is the unique person id",
        gt=0
    ),
    # aca esta la validacion, el body tiene que ser obligatorio, y el body es de tipo person, que a su vez es un json con los datos de la persona
    
    person:Person=Body(...),
    location:Location=Body(...)
):
    # para pasar varios body a la vez lo que hacemos es ponerlos en un diccionario y concatenarlos
    # eso se hace con el metodo update.  
    results=person.dict()
    results.update(location.dict())
    return results

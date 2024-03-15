from pydantic import BaseModel,Field

class PostValidate(BaseModel):
    name:str=Field(...,description="name of the person")
    age:int=Field(...,description="age of the person")

class UpdateFinder(BaseModel):
    name:str=Field(...)

class BasicTemplate(BaseModel):
    updates:str
    sequence:int
    count:int
    merge:bool
        


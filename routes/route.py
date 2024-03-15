from fastapi import APIRouter,Body
from schemas import schema
from database import db
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException,status
router = APIRouter()

@router.put('/insert')
def insert_Data(data:schema.PostValidate=Body(...,description="inserting data")): 
        if(db.add_Data(jsonable_encoder(data))):
            return {"RESPONSE":HTTPException(status_code=status.HTTP_200_OK)}
        else:
              return{"RESPONSE":HTTPException(status_code=status.HTTP_400_BAD_REQUEST)}
      
@router.get('/readdata')
def read_Data():
        return {"Response":db.read_Data(),
                "code":HTTPException(status_code=status.HTTP_200_OK)}


@router.post('/finddetails')
def findDetails(data:schema.UpdateFinder):
      return db.find_Details(data)  

@router.post('/update')
def update_Details(data:schema.UpdateFinder=Body(...)):
      return db.update_Details(data)
             
@router.delete("/deletedetails")
def deleteDetails(data:schema.UpdateFinder=Body(...)):
      return db.delete_Details(data)

@router.get('/query')
def queryparams(query:int=0):
      return {"RESPONSE":"NONE",
              "QUERY":query}

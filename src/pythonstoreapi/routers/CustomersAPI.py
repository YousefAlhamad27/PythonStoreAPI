
from fastapi import APIRouter,status,HTTPException,Depends
from Models.Customers import Customer
from typing import List,Dict, Any
from pydantic import BaseModel

router=APIRouter()

@router.get("/CustomersList",response_model=List[Customer])
async def GetCustomers():
    customers=await Customer.find_all().to_list()
    
    if customers ==None :
        raise HTTPException(status_code=500,detail="Server Problem")

    return customers
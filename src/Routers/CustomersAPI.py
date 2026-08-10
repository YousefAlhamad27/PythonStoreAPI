
from fastapi import APIRouter,status,HTTPException,Depends
from src.Models.Customers import Customer
from src.Auth import security
from src.Services import CustomerService
from typing import List,Dict, Any
from src import Util
from pydantic import BaseModel

router=APIRouter()

@router.get("/CustomersList",response_model=List[Customer])
async def GetCustomers(pageNumber:int=1,pageSize:int=10,token:str=Depends(security.oauth2_scheme)):
    token=Util.verify_access_token(token)
    
    if token is None:
            raise HTTPException(status_code=401,detail="Invalid token")

    customers=await CustomerService.GetCustomersList(pageNumber,pageSize)
    
    if customers ==None :
        raise HTTPException(status_code=500,detail="Server Problem")

    return customers
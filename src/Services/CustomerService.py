# from Schemas.CustomersDTOs import  
from fastapi import HTTPException

from src import Util
from src.Models.Customers import Customer
from typing import List,Dict, Any
from pydantic import BaseModel

async def GetCustomersList(pageNumber:int,pageSize:int)->List[Customer]:

    skipCount=(pageNumber-1)*pageSize
    try:
        customers=await Customer.find_all().skip(skipCount).limit(pageSize).to_list()
        return customers

    except Exception as exception:
        raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")   
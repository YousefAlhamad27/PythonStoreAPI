
from fastapi import APIRouter,status,HTTPException,Depends
from Models.Products import Product
from typing import List,Dict, Any
from pydantic import BaseModel

router=APIRouter()

class ProductCreateDTO(BaseModel):
      name:str
      category:str
      price:float
      stock:int
      attributes:Dict[str,Any]


@router.post("/Create-Product",status_code=status.HTTP_201_CREATED,response_model=Product)
async def createProduct(payload: ProductCreateDTO):

    lastProduct=await Product.find_all().sort("-id").first_or_none()
    if lastProduct:

        lastNumber=int(lastProduct.id.split("-")[1])
        nextNumber=lastNumber+1
 
    else:
        nextNumber=1

    newProductID=f"PROD-{nextNumber:03d}"    

 
    
    try:
        newProduct=Product(
                id=newProductID,name=payload.name,category=payload.category,price=payload.price
                ,stock=payload.stock,attributes=payload.attributes
                )
        await newProduct.insert()

    except Exception:
        raise HTTPException(status_code=500,detail="Server Issue")

    
    return newProduct
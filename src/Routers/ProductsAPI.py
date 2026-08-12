from Models.Users import User

from src import Util
from fastapi import APIRouter,status,HTTPException,Depends
from src.Models.Products import Product
from src.Auth import security
from src.Schemas.ProductsDTOs import ProductCreateDTO,ProductUpdateDTO,UpdateOptionalDTO,ProductResponse
from typing import Annotated, List,Dict, Any,Optional
from src.Services import ProductService
from pymongo import MongoClient
from pydantic import BaseModel,Field

router=APIRouter()

@router.post("/Create-Product",status_code=status.HTTP_201_CREATED,response_model=Product)
async def createProduct(payload: ProductCreateDTO,current_user:Annotated[User,Depends(security.get_current_user)]): 
    


    
    product=await ProductService.CreateProduct(payload)

    if product is None:
        raise HTTPException(status_code=500,detail="Server Problem")
    
    return product

@router.get("/GetProduct/{productID}",status_code=status.HTTP_200_OK)
async def getProduct(productID:str,current_user:Annotated[User,Depends(security.get_current_user)]):

    

    
       
    product=await ProductService.GetProductByID(productID)

    if product is None:
        raise HTTPException(status_code=404,detail="Product not found")
    return product   
       

 
        

#deleteOne() or deleteMany()
@router.delete("/Delete-Product/{productID}",status_code=status.HTTP_200_OK)
async def deleteProduct(productID:str, current_user: dict = Depends(security.get_current_user)):

     
     
     deleted=await ProductService.DeleteProduct(productID)

     if deleted==False:
            raise HTTPException(status_code=500,detail="Server Problem")
     return {"message":"Product Deleted successfully!"}
  
    
#pagination
@router.get("/ProductsList",response_model=List[Product])
async def GetProducts(current_user:Annotated[User,Depends(security.get_current_user)],pageNumber:int=1, pageSize:int=10)-> List[Product]:

    products=await ProductService.GetProducts(pageNumber,pageSize)
    if products is None:
        raise HTTPException(status_code=404,detail="No products found")

    return products

@router.put("/UpdateProduct",status_code=status.HTTP_200_OK)

async def updateProduct(payload:ProductUpdateDTO, current_user:Annotated[User,Depends(security.get_current_user)]):

    

    saved=await ProductService.UpdateProduct(payload)
    
    if saved ==False:
            raise HTTPException(status_code=500,detail="Server Problem")
    return {"message":"Product Updated successfully!"}
    



#allow one or more or all to be updated
@router.patch("/UpdateProductOptional",status_code=status.HTTP_200_OK)    
async def UpdateCategory(payload:UpdateOptionalDTO, current_user: dict = Depends(security.get_current_user)):

   

    saved=await ProductService.UpdateProductOptional(payload)

    if saved ==False:
        raise HTTPException(status_code=500,detail="Server Problem")

    return {"message":"Product Updated successfully!"}  
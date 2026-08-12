from src import Util
from fastapi import APIRouter,status,HTTPException,Depends
from src.Models.Products import Product
from src.Auth import security
from src.Schemas.ProductsDTOs import ProductCreateDTO,ProductUpdateDTO,UpdateOptionalDTO,ProductResponse
from typing import List,Dict, Any,Optional
from src.Services import ProductService
from pymongo import MongoClient
from pydantic import BaseModel,Field

router=APIRouter()

@router.post("/Create-Product",status_code=status.HTTP_201_CREATED,response_model=Product)
async def createProduct(payload: ProductCreateDTO,token:str=Depends(security.oauth2_scheme)): 

    token=Util.verify_access_token(token)

    if token is None:
        raise HTTPException(status_code=401,detail="Invalid token")


    
    product=await ProductService.CreateProduct(payload)

    if product is None:
        raise HTTPException(status_code=500,detail="Server Problem")
    
    return product

@router.get("/GetProduct/{productID}",status_code=status.HTTP_200_OK)
async def getProduct(productID:str,token:str=Depends(security.oauth2_scheme)):

    token=Util.verify_access_token(token)

    if token is None:
        raise HTTPException(status_code=401,detail="Invalid token")

    
       
    product=await ProductService.GetProductByID(productID)

    if product is None:
        raise HTTPException(status_code=404,detail="Product not found")
    return product   
       

 
        

#deleteOne() or deleteMany()
@router.delete("/Delete-Product/{productID}",status_code=status.HTTP_200_OK)
async def deleteProduct(productID:str,token:str=Depends(security.oauth2_scheme)):

     token=Util.verify_access_token(token)
     
     if token is None:
             raise HTTPException(status_code=401,detail="Invalid token")
     
     deleted=await ProductService.DeleteProduct(productID)

     if deleted==False:
            raise HTTPException(status_code=500,detail="Server Problem")
     return {"message":"Product Deleted successfully!"}
  
    
#pagination
@router.get("/ProductsList",response_model=List[Product])
async def GetProducts(pageNumber:int=1, pageSize:int=10,token:str=Depends(security.oauth2_scheme))-> List[Product]:

    token=Util.verify_access_token(token)

    if token is None:
        raise HTTPException(status_code=401,detail="Invalid token")

    products=await ProductService.GetProducts(pageNumber,pageSize)
    if products is None:
        raise HTTPException(status_code=404,detail="No products found")

    return products

@router.put("/UpdateProduct",status_code=status.HTTP_200_OK)

async def updateProduct(payload:ProductUpdateDTO,token:str=Depends(security.oauth2_scheme)):

    token=Util.verify_access_token(token)

    if token is None:
        raise HTTPException(status_code=401,detail="Invalid token")

    saved=await ProductService.UpdateProduct(payload)
    
    if saved ==False:
            raise HTTPException(status_code=500,detail="Server Problem")
    return {"message":"Product Updated successfully!"}
    



#allow one or more or all to be updated
@router.patch("/UpdateProductOptional",status_code=status.HTTP_200_OK,dependencies=[Depends(Util.get_current)])    
async def UpdateCategory(payload:UpdateOptionalDTO,token:str=Depends(security.oauth2_scheme)):

    token=Util.verify_access_token(token)

    if token is None:
        raise HTTPException(status_code=401,detail="Invalid token")

    saved=await ProductService.UpdateProductOptional(payload)

    if saved ==False:
        raise HTTPException(status_code=500,detail="Server Problem")

    return {"message":"Product Updated successfully!"}  
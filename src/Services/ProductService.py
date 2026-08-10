from src.Schemas.ProductsDTOs import ProductCreateDTO,ProductUpdateDTO,UpdateOptionalDTO,ProductResponse
from fastapi import HTTPException

from src import Util
from src.Models.Products import Product
from typing import List,Dict, Any
from pydantic import BaseModel


async def CreateProduct(payload: ProductCreateDTO)->Product:

         
    
     
        
        try:
            lastProduct=await Product.find_all().sort("-id").first_or_none()
            if lastProduct:
            
                    lastNumber=int(lastProduct.productID.split("-")[1])
                    nextNumber=lastNumber+1
             
            else:
                    nextNumber=1
            
            newProductID=f"PROD-{nextNumber:03d}"      
            
            newProduct=Product(
                     productID=newProductID,name=payload.name,category=payload.category,price=payload.price
                    ,stock=payload.stock,attributes=payload.attributes
                    )
             
            await newProduct.insert()
    
        except Exception as exception:
            raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")

        return newProduct

async def DeleteProduct(productID:str)->bool:
      
    try:
        product=await Product.find_one(Product.productID==productID)

        if product==None:
            raise HTTPException(status_code=404,detail="Product does not exist")
        
        await product.delete()
        return True

    except Exception as exception:
        raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")
    

async def GetProducts(pageNumber:int=1, pageSize:int=10)-> List[Product]:

    skipCount=(pageNumber-1)*pageSize

    try:
         products=await Product.find_all().skip(skipCount).limit(pageSize).to_list()
         return products   
    
    except Exception as exception:
            raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")
         
    

async def UpdateProduct(payload:ProductUpdateDTO)->Product:

    try:
        product=await Product.find_one(Product.productID== payload.productID)

        if product ==None:
             raise HTTPException(status_code=404,detail="Product does not exist")
        
        product.name=payload.name
        product.attributes=payload.attributes
        product.stock=payload.stock
        product.price=payload.price
        product.category=payload.category

        #await product.update()
        await product.save()

    except Exception as exception:
        raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")

    return product 

async def GetProductByID(productID:str)->Product:

    try:
        product=await Product.find_one(Product.productID==productID)

        return None if product is None else product
    except Exception as exception:
        raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")

async def UpdateProductOptional(payload:UpdateOptionalDTO)->Product:
          try:
            product =await Product.find_one(Product.productID==payload.productID)
    
            if product==None:
                raise HTTPException(status_code=404,detail="Product does not exist")
    
            # updateData= payload.model_dump(exclude_unset=True)
    
            # updateData.pop("ProductID",None)
    
            # for key,value in updateData.items():
            #      setattr(product,key,value)
    
    
            if payload.category!=None and payload.category!="":
               product.category=payload.category
    
            if payload.name!=None and payload.name!="":
                       product.name=payload.name
    
            if  payload.attributes!=None:
                        product.attributes=payload.attributes
    
            if payload.price!=None and payload.price!=0:
                       product.price=payload.price
    
            if payload.stock!=None:
                       product.stock=payload.stock   
    
            await product.save()
            return True
          
          except Exception as exception:
            raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")    
        
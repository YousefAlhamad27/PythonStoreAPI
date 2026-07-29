
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

class ProductUpdateDTO(BaseModel):
      id:str
      name:str
      category:str
      price:float
      stock:int
      attributes:Dict[str,Any]      

#query parameter vs path variable
#create another system id and forget about id
@router.post("/Create-Product",status_code=status.HTTP_201_CREATED,response_model=Product)
async def createProduct(payload: ProductCreateDTO): 




    lastProduct=await Product.find_all().sort("-system_id").first_or_none()
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

    except Exception as exception:
        raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")

    
    return newProduct


#deleteOne() or deleteMany()
@router.delete("/Delete-Product",status_code=status.HTTP_200_OK)
async def deleteProduct(productID:str):
      
     
  
     try:
        product = await Product.get(productID)
        if not product :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product Not Found")
           
        await product.delete()
        return {"message":f"Product {productID} delete successfully!"}
     except Exception as exception:
        raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")


#pagination
@router.get("/ProductsList",response_model=List[Product])
async def GetCustomers():
    products=await Product.find_all().to_list()
    
    if products ==None :
        raise HTTPException(status_code=500,detail="Server Problem")

    return products
@router.put("/UpdateProduct",status_code=status.HTTP_200_OK)

async def updateProduct(payload:ProductUpdateDTO):

    try:
        product=await Product.get(payload.id)

        if product ==None:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product does not exist")
        
        product.name=payload.name
        product.attributes=payload.attributes
        product.stock=payload.stock
        product.price=payload.price
        product.category=payload.category

        #await product.update()
        await product.save()

        return {"message":"Product Updated successfully!"}
    except Exception as exception:
        raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")


class UpdateCategoryDTO(BaseModel):
    id:str
    category:str

#allow one or more or all to be updated
@router.patch("/UpdateCategory",status_code=status.HTTP_200_OK)    
async def UpdateCategory(payload:UpdateCategoryDTO):

    try:
        product =await Product.get(payload.id)

        if product==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product does not exist")

        product.category=payload.category

        await product.save()
        return {"message":"Category Updated successfully!"}
    except Exception as exception:
        raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")        
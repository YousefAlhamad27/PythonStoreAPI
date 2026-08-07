from fastapi import APIRouter,status,HTTPException,Depends
from src.Models.Products import Product
from src.Schemas.ProductsDTOs import ProductCreateDTO,ProductUpdateDTO,UpdateOptionalDTO,ProductResponse
from typing import List,Dict, Any,Optional
from pymongo import MongoClient
from pydantic import BaseModel,Field

router=APIRouter()

# class ProductCreateDTO(BaseModel):
#       name:str
#       category:str
#       price:float
#       stock:int
#       attributes:Dict[str,Any]

# class ProductResponse(BaseModel):
#     productID: str 
#     name: str
#     category: str
#     price: float
#     stock: int
#     attributes: Dict[str, Any]      

# class UpdateOptionalDTO(BaseModel):
#     productID:str
#     category:Optional[str]=None
#     name: Optional[str]=None
#     category: Optional[str]=None
#     price: Optional[float]=None
#     stock: Optional[int]=None
#     attributes: Optional[Dict[str, Any]]= None

# class ProductUpdateDTO(BaseModel):
#       productID:str
#       name:str
#       category:str
#       price:float
#       stock:int
#       attributes:Dict[str,Any]      

#query paramter vs path variable
#create another system id and forget about _id
@router.post("/Create-Product",status_code=status.HTTP_201_CREATED,response_model=Product)
async def createProduct(payload: ProductCreateDTO): 




    lastProduct=await Product.find_all().sort("-id").first_or_none()
    if lastProduct:

        lastNumber=int(lastProduct.productID.split("-")[1])
        nextNumber=lastNumber+1
 
    else:
        nextNumber=1

    newProductID=f"PROD-{nextNumber:03d}"    

 
    
    try:
        newProduct=Product(
                 productID=newProductID,name=payload.name,category=payload.category,price=payload.price
                ,stock=payload.stock,attributes=payload.attributes
                )
         
        await newProduct.insert()

    except Exception as exception:
        raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")

    
    return newProduct

@router.get("/GetProduct/{productID}",status_code=status.HTTP_200_OK)
async def getProduct(productID:str):

    try:
       if productID == "":
         raise HTTPException(status_code=400)
       
       product= await Product.find_one(Product.productID==productID)
       #product=await Product.get(productID)
       if product == None:
        raise HTTPException(status_code=404)

       return product      

    except Exception as e:
         raise HTTPException(status_code=500,detail=f"Server Issue: {str(e)}")
        

#deleteOne() or deleteMany()
@router.delete("/Delete-Product/{productID}",status_code=status.HTTP_200_OK)
async def deleteProduct(productID:str):
      
     
  
     try:
         
        
           
        await Product.find_one(Product.productID==productID).delete()

        return {"message":f"Product {productID} delete successfully!"}
     except Exception as exception:
        raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")

#pagination
@router.get("/ProductsList",response_model=List[Product])
async def GetProducts(pageNumber:int=1, pageSize:int=10)-> List[Product]:

    skipCount=(pageNumber-1)*pageSize

    products=await Product.find_all().skip(skipCount).limit(pageSize).to_list()
    
    if products ==None :
        raise HTTPException(status_code=500,detail="Server Problem")

    return products

@router.put("/UpdateProduct",status_code=status.HTTP_200_OK)

async def updateProduct(payload:ProductUpdateDTO):

    try:
        product=await Product.find_one(Product.productID== payload.productID)

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




#allow one or more or all to be updated
@router.patch("/UpdateProductOptional",status_code=status.HTTP_200_OK)    
async def UpdateCategory(payload:UpdateOptionalDTO):

    try:
        product =await Product.find_one(Product.productID==payload.productID)

        if product==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product does not exist")

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
        return {"message":"Category Updated successfully!"}
    except Exception as exception:
        raise HTTPException(status_code=500,detail=f"Server Issue: {str(exception)}")  
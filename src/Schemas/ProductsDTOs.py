from pydantic import BaseModel
from typing import List,Dict, Any,Optional

class ProductCreateDTO(BaseModel):
      name:str
      category:str
      price:float
      stock:int
      attributes:Dict[str,Any]

class ProductResponse(BaseModel):
    productID: str 
    name: str
    category: str
    price: float
    stock: int
    attributes: Dict[str, Any]      


class ProductUpdateDTO(BaseModel):
      productID:str
      name:str
      category:str
      price:float
      stock:int
      attributes:Dict[str,Any]  


class UpdateOptionalDTO(BaseModel):
    productID:str
    category:Optional[str]=None
    name: Optional[str]=None
    category: Optional[str]=None
    price: Optional[float]=None
    stock: Optional[int]=None
    attributes: Optional[Dict[str, Any]]= None      
from beanie import Document
from pydantic import Field
from typing import List,Dict, Any
from datetime import datetime


class Product(Document):
    id:str=Field(alias="_id")        
    name:str
    category:str
    price:float
    stock:int
    attributes:Dict[str,Any]= Field(default_factory=dict)

    class Settings:
        name="Products"
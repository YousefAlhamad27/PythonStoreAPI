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
    tags:List[str]
    specs:dict[str,Any]

    class Settings:
        name="Products"
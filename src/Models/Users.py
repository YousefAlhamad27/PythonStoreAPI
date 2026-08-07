from beanie import Document
from pydantic import Field
from typing import List,Dict, Any
from datetime import datetime


class User(Document):
  
    username: str
    email: str
    password:str
    memberSince: datetime
    address:dict[str,Any]
    orders:List[Any]
    class Settings:
            name="Users"
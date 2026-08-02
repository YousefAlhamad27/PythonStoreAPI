from beanie import Document
from pydantic import Field
from typing import List,Dict, Any
from datetime import datetime

class Customer(Document):
    username:str
    status:str
    age:int
    score:int

    class Settings:
        name="Customers"
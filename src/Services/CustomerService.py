# from Schemas.CustomersDTOs import  
from fastapi import HTTPException

from src import Util
from src.Models.Customers import Customer
from typing import List,Dict, Any
from pydantic import BaseModel
from src import Util
from src.Models.Users import User
from typing import List,Dict, Any
from pydantic import BaseModel


async def FindUserByUsername(username:str)->User:

    try:
        user=await User.find_one(User.username==username)
        return user
    except Exception as e:
        print(f"Error finding user by username: {e}")
        return None

async def FindUserByID(userID:str)->User:

    try:
        user= await User.get(userID)
        return user
    except Exception as e:
         
        return None
    





from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from src import  Util


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="UserAPI/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
   
    user =  Util.verify_access_token(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user
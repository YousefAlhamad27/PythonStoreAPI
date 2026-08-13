from src.Models.Users import User

from src.Auth import security
from fastapi import APIRouter,status,HTTPException,Depends
from src.Schemas.UsersDTOs import UserLogin
# from src.Models.Customers import Customer
from typing import Annotated, List,Dict, Any

from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from src import Util
from src.Services import UserService

router=APIRouter()


@router.post("/UserAPI/login",status_code=status.HTTP_200_OK)
async def login(payload:Annotated[OAuth2PasswordRequestForm, Depends()]):

    #check login credentials
    user=await UserService.FindUserByUsername(payload.username)

    if user is None:
        raise HTTPException(status_code=404,detail="User not found")

    if not Util.verify_password(payload.password,user.password):
        raise HTTPException(status_code=401,detail="Invalid password")

     #if login is successful, return a token

    access_token=Util.create_access_token(user.username,str(user.id),"User")
    
    if access_token is None:
        raise HTTPException(status_code=500,detail="Could not create access token")
    
    return {"access_token":access_token,"token_type":"bearer"}

@router.get("/UserAPI/me",status_code=status.HTTP_200_OK)

async def getCurrentUser(current_user:Annotated[User,Depends(security.get_current_user)]):

     

    

    if current_user is None:
        raise HTTPException(status_code=404,detail="User not found")

    

    return current_user

@router.get("/UserAPI/GetUser",status_code=status.HTTP_200_OK)

async def getCurrentUser(username:str,current_user:Annotated[User,Depends(security.get_current_user)]):

     
    user=await UserService.FindUserByUsername(username)
    

    if user is None:
        raise HTTPException(status_code=404,detail="User not found")

    

    return user

   
    
    


    

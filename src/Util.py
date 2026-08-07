
from typing import Dict
from datetime import datetime, timedelta, timezone
from internal.config import settings
from typing import Dict, Any
import jwt
from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def create_access_token(username:str,userID:str,userRole:str):
    try:
        data:Dict[str,Any] = {
        "username": username,
        "sub": userID,
        "user_role": userRole,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }

        to_encode = data.copy()
   
    

     
        encoded_jwt = jwt.encode(to_encode,settings.TOKEN_SECRET_KEY, algorithm= "HS256")
        return encoded_jwt
    except Exception as e:
         
        return None

    

def verify_access_token(token:str):
    try:
        payload = jwt.decode(token, settings.TOKEN_SECRET_KEY, algorithms=["HS256"])
        username: str = payload.get("username")
        user_id: str = payload.get("sub")
        user_role: str = payload.get("user_role")

        if username is None or user_id is None or user_role is None:
            return None
        
        return payload
    
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
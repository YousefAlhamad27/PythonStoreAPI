
from fastapi import APIRouter,status,HTTPException,Depends
from pydantic import BaseModel

router=APIRouter()

Message=""
class MessagePayload(BaseModel):
    message:str

@router.get("/")

def home():
    return{"Message" :  f"Okay  {Message}"  }




@router.post("/",status_code=status.HTTP_201_CREATED)

def addMessage(payload:MessagePayload):
    global Message
    Message=payload.message
    if payload.message== 'error':
        raise HTTPException( 
        status_code=status.HTTP_400_BAD_REQUEST,
        Message="Bad Data"
    )

    return status.HTTP_201_CREATED, {"Status": "Updated Successfully!"}


def verify_token(token: str):
    if token != "supersecret":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True

@router.get("/secure-Data",status_code=status.HTTP_200_OK,
         dependencies=[Depends(verify_token)])
def getSecureData():
    return {"Data": "Top Secret Information"}
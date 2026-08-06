from pydantic import BaseModel



class UserAuth(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(UserAuth):
    hashed_password: str
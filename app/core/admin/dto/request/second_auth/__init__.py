from pydantic import BaseModel


class SecondAuthRequest(BaseModel):
    auth_code: str


class UpdateSecondAuthRequest(BaseModel):
    auth_code: str
    new_auth_code: str

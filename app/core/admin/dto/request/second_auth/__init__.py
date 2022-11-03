from pydantic import BaseModel


class SecondAuthRequest(BaseModel):
    auth_code: str

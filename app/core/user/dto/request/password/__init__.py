from pydantic import BaseModel


class UpdatePasswordRequest(BaseModel):
    password: str
    new_password: str
from pydantic import BaseModel, validator, constr
from fastapi import status, HTTPException


class UserUpdateProfileRequest(BaseModel):
    name: str
    email: constr()
    phone_num: str

    @validator('email')
    def check_email(cls, email):
        if '@' not in email or '.' not in email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="이메일이 형식에 맞지 않습니다!")
        return email

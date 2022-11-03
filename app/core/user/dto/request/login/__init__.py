from fastapi import HTTPException, status
from pydantic import BaseModel, validator, constr


class UserLoginRequest(BaseModel):
    email: constr()
    password: constr()

    @validator('email')
    def check_email(cls, email):
        if '@' not in email or '.' not in email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="이메일이 형식에 맞지 않습니다!")
        return email

    @validator('password')
    def check_password(cls, password):
        if not 8 < len(password) < 15:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='비밀번호는 8자 이상 15자 이하여야 합니다!')
        return password

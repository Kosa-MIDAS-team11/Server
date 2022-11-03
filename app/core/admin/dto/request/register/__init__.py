from pydantic import BaseModel, validator, constr
from fastapi import status, HTTPException


class AdminRegisterRequest(BaseModel):
    name: constr()
    email: constr()
    phone_num: constr()
    password: constr()

    @validator('name')
    def check_name(cls, name):
        if not 2 <= len(name) <= 5 or name in ['', ' ', None]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='이름은 1자 이상 5자 이하여야 합니다!')
        return name

    @validator('email')
    def check_email(cls, email):
        if '@' not in email or '.' not in email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="이메일이 형식에 맞지 않습니다!")
        return email

    @validator('phone_num')
    def check_phone_num(cls, phone_num):
        if len(phone_num) != 11 or phone_num[:3] != "010" or '-' in phone_num:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='전화번호는 -를 제외한 11자이여야 합니다!')
        return phone_num

    @validator('password')
    def check_password(cls, password):
        if not 8 <= len(password) <= 15:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='비밀번호는 8자 이상 15자 이하여야 합니다!')
        return password

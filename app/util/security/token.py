from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status

from app.config import JWTConfig


def generate_access_token(email: str):
    exp = datetime.utcnow() + timedelta(hours=int(JWTConfig.ACCESS_TIMEOUT))
    encoded_jwt = jwt.encode(payload={'exp': exp, 'sub': email}, key=JWTConfig.SECRET)
    return encoded_jwt


def get_email(token: str):
    payload = jwt.decode(jwt=token, key=JWTConfig.SECRET, algorithms=JWTConfig.ALGORITHM)
    email = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="유저를 찾을 수 없습니다!")
    return email


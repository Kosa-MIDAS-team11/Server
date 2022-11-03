from fastapi import HTTPException, status

from sqlalchemy.orm import Session
from app.util.dao.models.user import User


def check_id(account_id: str, session: Session):
    user = session.query(User.email).filter(User.email == account_id)

    if user.all():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="아이디가 이미 존재합니다!")


from uuid import uuid4

from sqlalchemy.orm import Session
from app.util.dao.models.user import User


def save_user(session: Session, email: str, name: str, password: str, phone_num: str, is_admin: bool):
    session.add(
        User(
            name=name,
            email=email,
            password=password,
            phone_num=phone_num,
            is_admin=is_admin
        )
    )

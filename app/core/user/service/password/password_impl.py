from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.core.user.service.password import UserUpdatePassword
from app.util.dao.models.user import User
from app.util.security.token import get_email
from app.util.security.password import match_password, encode_password


class UserUpdatePasswordImpl(UserUpdatePassword):

    def execute(self, session: Session, token: str, password: str, new_password: str):
        user = session.query(User).filter(User.email == get_email(token)).one()

        if match_password(password, user.password):
            user.password = encode_password(new_password)

        else:
            raise HTTPException(400, detail='비밀번호가 일치하지 않습니다!')


user_update_password_impl = UserUpdatePasswordImpl()

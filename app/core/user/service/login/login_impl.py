from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.core.user.service.login import UserLoginService

from app.util.dao.models.user import User
from app.util.security.password import match_password

from app.util.security.token import generate_access_token


class UserLoginImpl(UserLoginService):

    def execute(self, session: Session, email: str, password: str):

        user = session.query(User.password, User.is_admin).filter(User.email == email)

        if user.scalar() is None:
            raise HTTPException(404, detail='유저가 존재하지 않습니다!')

        user = user.one()

        if not match_password(password, user['password']):
            raise HTTPException(400, detail='비밀번호를 확인해 주세요!')

        return generate_access_token(email)


user_login_impl = UserLoginImpl()

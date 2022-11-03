from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.admin.service.fire_user import FireUserService

from app.util.dao.models.user import User
from app.util.dao.models.department.my_department import MyDepartment
from app.util.security.token import get_email


class FireUserImpl(FireUserService):

    def execute(self, session: Session, token, user_email):
        is_admin = session.query(User.is_admin).filter(User.email == get_email(token)).one()['is_admin']

        if not is_admin:
            raise HTTPException(403, detail="역할이 맞지 않습니다!")

        my_department = session.query(MyDepartment).filter(MyDepartment.user_email == user_email).one()

        session.delete(my_department)


fire_user_impl = FireUserImpl()

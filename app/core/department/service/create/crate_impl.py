from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.util.dao.models.user import User
from app.util.dao.models.department.department import Department
from app.util.dao.models.department.my_department import MyDepartment

from app.util.security.token import get_email

from app.core.department.service.create import CreateDepartmentService


class CreateDepartmentImpl(CreateDepartmentService):

    def execute(self, session: Session, token: str, name: str, location: str):
        is_admin = session.query(User.is_admin).filter(User.email == get_email(token)).one()['is_admin']

        if not is_admin:
            raise HTTPException(403, '올바르지 않은 역할입니다')

        department_id = uuid4().bytes

        department = self.__create_department(department_id, name, location)

        my_department = self.__create_my_department(department_id, get_email(token))

        session.add(department)
        session.add(my_department)

    @staticmethod
    def __create_department(_id, name, location):
        return Department(
            department_id=_id,
            name=name,
            location=location
        )

    @staticmethod
    def __create_my_department(_id, email):
        return MyDepartment(
            department_id=_id,
            user_email=email,
            is_manager=True
        )


create_department_impl = CreateDepartmentImpl()

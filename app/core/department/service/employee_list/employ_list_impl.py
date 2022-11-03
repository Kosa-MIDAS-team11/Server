from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.department.service.employee_list import EmployeeListService
from app.util.dao.models.user import User
from app.util.dao.models.department.my_department import MyDepartment
from app.util.security.token import get_email


class EmployListImpl(EmployeeListService):
    def execute(self, session: Session, token, department_id: str):
        is_admin = session.query(User.is_admin).filter(User.email == get_email(token)).one()['is_admin']

        if not is_admin:
            raise HTTPException(403, "역할이 올바르지 않습니다!")

        user_list = session.query(User).select_from(User).join(MyDepartment.department_id == department_id).all()

        response = []
        for i in user_list:
            response.append(
                {
                    'name': i.department_name,
                    'email': i.email,
                    'phone_num': i.phone_num
                }
            )

        print(response)


employ_list_impl = EmployListImpl()

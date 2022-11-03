from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.core.department.service.list import DepartmentListService

from app.util.dao.models.department.department import Department
from app.util.dao.models.department.my_department import MyDepartment
from app.util.dao.models.user import User

from app.util.security.token import get_email


class DepartmentListImpl(DepartmentListService):

    def execute(self, session: Session, token):
        if not session.query(User.is_admin).filter(User.email == get_email(token)).one()['is_admin']:
            raise HTTPException(403, '맞지 않은 역할입니다.')

        department_list = session.query(
            Department.department_id,
            Department.department_name,
            Department.location
        ).all()

        return department_list


department_list_impl = DepartmentListImpl()

from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.core.department.service.list import DepartmentListService

from app.util.dao.models.department.department import Department
from app.util.dao.models.user import User

from app.util.security.token import get_email


class DepartmentListImpl(DepartmentListService):

    def execute(self, session: Session, token):

        if not session.query(User.is_admin).filter(User.email == get_email(token)).one()['is_admin']:
            raise HTTPException(403, '맞지 않은 역할입니다.')

        response = []
        for i in session.query(Department).all():
            response.append(
                {
                    'department_id': i.department_id,
                    'name': i.name,
                    'location': i.location,
                }
            )
        return {
            'department_list': response
        }


department_list_impl = DepartmentListImpl()

from sqlalchemy.orm import Session
from app.util.dao.models.user import User
from app.util.dao.models.department.department import Department
from app.util.dao.models.department.my_department import MyDepartment

from app.core.employee.service import EmployeeListService


class EmployListImpl(EmployeeListService):

    def execute(self, session: Session, token: str, department_id: int):
        return session.query(
            User.name,
            User.email,
            User.phone_num
        ).join(
            User.email == MyDepartment.user_email,
        ).where(
            MyDepartment.department_id == department_id
        ).all()


employ_list_impl = EmployListImpl()

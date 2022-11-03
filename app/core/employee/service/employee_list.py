from sqlalchemy.orm import Session
from app.util.dao.models.user import User
from app.util.dao.models.department.department import Department
from app.util.dao.models.department.my_department import MyDepartment

from app.core.employee.service import EmployeeListService


class EmployListImpl(EmployeeListService):

    def execute(self, session: Session, token: str, department_id: int):
        user_list = session.query(
            MyDepartment.department_id,
            User.name,
            User.email,
            User.phone_num
        ).select_from(
            User
        ).join(
            MyDepartment, User.email == MyDepartment.user_email
        ).all()



        return {
            'employee_list': user_list
        }


employ_list_impl = EmployListImpl()

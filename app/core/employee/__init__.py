from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.employee.request.list import EmployeeListRequest

from app.core.employee.service import duc_admin_register

from app.core.employee.service.employee_list import employ_list_impl

from app.util.dao import session_scope

employee_router = APIRouter(
    prefix='/employee'
)

_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@employee_router.get('/list')
def get_employ_list(reqeust: EmployeeListRequest, token: str = Depends(_oauth2_scheme)):
    with session_scope() as session:
        return duc_admin_register(
            employ_list_impl, session, token, reqeust.department_id
        )

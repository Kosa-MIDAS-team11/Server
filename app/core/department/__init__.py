from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer

from app.util.dao import session_scope

from app.core.department.request.create import CreateDepartmentRequest

from app.core.department.service.create import duc_create_department

from app.core.department.service.create.crate_impl import create_department_impl

department_router = APIRouter(
    prefix='/department'
)

_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@department_router.post('/', status_code=status.HTTP_201_CREATED)
def create_department(reqeust: CreateDepartmentRequest, token: str = Depends(_oauth2_scheme)):
    with session_scope() as session:
        duc_create_department(create_department_impl, session, token, reqeust.name, reqeust.location)

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer

from app.util.dao import session_scope

from app.core.department.request.create import CreateDepartmentRequest

from app.core.department.service.create import duc_create_department
from app.core.department.service.list import duc_query_department_list

from app.core.department.service.create.crate_impl import create_department_impl
from app.core.department.service.list.list_impl import department_list_impl

department_router = APIRouter(
    prefix='/department'
)

_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@department_router.post('/', status_code=status.HTTP_201_CREATED)
def create_department(reqeust: CreateDepartmentRequest, token: str = Depends(_oauth2_scheme)):
    with session_scope() as session:
        duc_create_department(create_department_impl, session, token, reqeust.name, reqeust.location)


@department_router.get('/list')
def create_department(token: str = Depends(_oauth2_scheme)):
    with session_scope() as session:
        return duc_query_department_list(department_list_impl, session, token)


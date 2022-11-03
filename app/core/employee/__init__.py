from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.core.employee.request.list import EmployeeListRequest

from app.core.employee.service import duc_admin_register

from app.core.employee.service.employee_list import employ_list_impl
from app.util.security.token import get_email

from app.util.dao import session_scope
from app.util.dao.models.work.my_work_date import WorkDate

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


from pydantic import BaseModel


class Comment(BaseModel):
    context: str


@employee_router.put('/log')
def work_go_home(comment: Comment, token: str = Depends(_oauth2_scheme)):
    from datetime import datetime, timedelta
    with session_scope() as session:

        work_date = session.query(WorkDate).filter(WorkDate.user_email == get_email(token))

        if work_date.start_at is None:
            work_date.work_day = (datetime.utcnow() + timedelta(hours=9)).date()
            WorkDate.start_at = (datetime.utcnow() + timedelta(hours=9)).time()
            WorkDate.todo = comment.context

        else:
            WorkDate.end_at = (datetime.utcnow() + timedelta(hours=9)).time()
            WorkDate.done = comment.context

        session.commit()

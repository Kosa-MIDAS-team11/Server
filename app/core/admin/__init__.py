from fastapi import status, APIRouter, Depends

from fastapi.security import OAuth2PasswordBearer

from app.util.dao import session_scope

from app.core.admin.dto.request.register import AdminRegisterRequest
from app.core.admin.dto.request.second_auth import SecondAuthRequest, UpdateSecondAuthRequest

from app.core.admin.service.register import duc_admin_register
from app.core.admin.service.second_auth import duc_second_auth_service, duc_update_second_auth_code_service

from app.core.admin.service.register.register_impl import admin_register_impl
from app.core.admin.service.second_auth.second_auth_impl import second_auth_service_impl
from app.core.admin.service.second_auth.update_second_impl import update_second_auth_code_impl

_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

admin_router = APIRouter(
    prefix='/admin'
)


@admin_router.post('/', status_code=status.HTTP_201_CREATED)
def admin_register(request: AdminRegisterRequest):
    with session_scope() as session:
        return duc_admin_register(
            admin_register_impl, session,
            request.email, request.name, request.password, request.phone_num, True
        )


@admin_router.post('/second-auth')
def admin_second_auth(request: SecondAuthRequest):
    with session_scope() as session:
        return duc_second_auth_service(
            second_auth_service_impl, session, request.auth_code
        )


@admin_router.put('/second-auth')
def update_second_auth_code(request: UpdateSecondAuthRequest,token: str = Depends(_oauth2_scheme)):
    with session_scope() as session:
        return duc_update_second_auth_code_service(
            update_second_auth_code_impl, session,
            token, request.auth_code, request.new_auth_code
        )

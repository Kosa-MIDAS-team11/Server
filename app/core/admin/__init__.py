from fastapi import status, APIRouter

from app.util.dao import session_scope

from app.core.admin.dto.request.register import AdminRegisterRequest
from app.core.admin.dto.request.second_auth import SecondAuthRequest

from app.core.admin.service.register import duc_admin_register
from app.core.admin.service.second_auth import duc_second_auth_service

from app.core.admin.service.register.register_impl import admin_register_impl
from app.core.admin.service.second_auth.second_auth_impl import second_auth_service_impl

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

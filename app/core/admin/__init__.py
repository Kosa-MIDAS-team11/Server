from fastapi import status, APIRouter

from app.util.dao import session_scope

from app.core.admin.dto.request.register import AdminRegisterRequest

from app.core.admin.service.register import duc_admin_register

from app.core.admin.service.register.register_impl import admin_register_impl

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



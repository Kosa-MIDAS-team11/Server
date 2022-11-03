from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.user.dto.request.login import UserLoginRequest
from app.core.user.dto.request.register import UserRegisterRequest
from app.core.user.dto.request.profile import UserUpdateProfileRequest
from app.core.user.dto.request.password import UpdatePasswordRequest

from app.core.user.service.login import duc_user_login
from app.core.user.service.login.login_impl import user_login_impl

from app.core.user.service.register import duc_user_register
from app.core.user.service.register.register_impl import user_register_impl

from app.core.user.service.profile import duc_user_update_profile
from app.core.user.service.profile.profile_impl import user_update_profile_impl

from app.core.user.service.password import duc_user_update_password
from app.core.user.service.password.password_impl import user_update_password_impl

from app.util.dao import session_scope

user_router = APIRouter(
    prefix='/user'
)

_oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@user_router.post('/')
def user_register(request: UserRegisterRequest):
    with session_scope() as session:
        return duc_user_register(
            user_register_impl, session,
            request.email, request.name, request.password, request.phone_num, False
        )


@user_router.post('/auth')
def user_login(request: UserLoginRequest):
    with session_scope() as session:
        return duc_user_login(
            user_login_impl, session, request.email, request.password
        )


@user_router.patch('/profile', status_code=status.HTTP_200_OK)
def user_update_profile(request: UserUpdateProfileRequest, token: str = Depends(_oauth2_scheme)):
    with session_scope() as session:
        return duc_user_update_profile(
            user_update_profile_impl, session,
            token, request.name, request.email, request.phone_num
        )


@user_router.patch('/password', status_code=status.HTTP_204_NO_CONTENT)
def user_update_password(request: UpdatePasswordRequest, token: str = Depends(_oauth2_scheme)):
    with session_scope() as session:
        duc_user_update_password(
            user_update_password_impl, session,
            token, request.password, request.new_password
        )

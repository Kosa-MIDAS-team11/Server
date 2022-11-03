from ..register import AdminRegisterService
from app.util.dao.cqrs.query.user import check_id
from app.util.dao.cqrs.command.user import save_user

from app.util.security.password import encode_password
from app.util.security.token import generate_access_token


class UserRegisterImpl(AdminRegisterService):

    def execute(self, session, email: str, name: str, password: str, phone_num: str, is_admin: bool):
        check_id(email, session)
        password = encode_password(password)
        save_user(session, email, name, password, phone_num, is_admin)

        return generate_access_token(email)


user_register_impl = UserRegisterImpl()

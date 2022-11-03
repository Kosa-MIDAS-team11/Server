from sqlalchemy.orm import Session

from app.core.admin.service.second_auth import UpdateSecondAuthService

from app.util.dao.models.user import User
from app.util.dao.models.code import Code

from app.util.security.password import encode_password, match_password
from app.util.security.token import get_email


class UpdateSecondAuthCodeImpl(UpdateSecondAuthService):

    def execute(self, session: Session, token: str, auth_code: str, new_auth_code: str):
        is_admin = session.query(User.is_admin).filter(User.email == get_email(token)).one()['is_admin']
        origin_code = session.query(Code).one()

        if is_admin and match_password(auth_code, origin_code.auth_code):
            origin_code.auth_code = encode_password(new_auth_code)
            session.commit()


update_second_auth_code_impl = UpdateSecondAuthCodeImpl()

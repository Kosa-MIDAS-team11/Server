from sqlalchemy.orm import Session

from app.core.user.service.profile import UpdateUserProfile
from app.util.dao.models.user import User

from app.util.security.token import get_email, generate_access_token


class UpdateUserProfileImpl(UpdateUserProfile):

    def execute(self, session: Session, token: str, name: str, email: str, phone_num: str):  # TODO 예외 처리
        user = session.query(User).filter(User.email == get_email(token)).one()

        user.email = email
        user.name = user.name if (not 2 <= len(name) <= 5) else name
        user.phone_num = user.phone_num if len(phone_num) != 11 or phone_num[
                                                                   :3] != "010" or '-' in phone_num else phone_num

        session.commit()

        return generate_access_token(email)


user_update_profile_impl = UpdateUserProfileImpl()

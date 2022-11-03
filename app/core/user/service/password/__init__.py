from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class UserUpdatePassword(ABC):

    @abstractmethod
    def execute(self, session: Session, token: str,password: str, new_password: str):
        pass


def duc_user_update_password(service_impl: UserUpdatePassword, session: Session, token: str,password: str, new_password: str):
    return service_impl.execute(session, token,password, new_password)

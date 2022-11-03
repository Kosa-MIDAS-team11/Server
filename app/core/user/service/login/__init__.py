from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class UserLoginService(ABC):

    @abstractmethod
    def execute(self, session: Session, email: str, password: str):
        pass


def duc_user_login(service_impl: UserLoginService, session: Session, email: str, password: str):
    return service_impl.execute(session, email, password)

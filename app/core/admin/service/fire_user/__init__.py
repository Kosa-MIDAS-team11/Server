from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class FireUserService(ABC):

    @abstractmethod
    def execute(self, session, token, email):
        pass


def duc_fire_user(service_impl: FireUserService, session: Session, token: str, email: str):
    return service_impl.execute(session, token, email)

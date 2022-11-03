from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class SecondAuthService(ABC):

    @abstractmethod
    def execute(self, session: Session, auth_code: str):
        pass


def duc_second_auth_service(service_impl: SecondAuthService, session: Session, auth_code: str):
    return service_impl.execute(session, auth_code)
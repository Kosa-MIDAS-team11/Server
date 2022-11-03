from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class SecondAuthService(ABC):

    @abstractmethod
    def execute(self, session: Session, auth_code: str):
        pass


class UpdateSecondAuthService(ABC):

    @abstractmethod
    def execute(self, session: Session, token: str, auth_code: str, new_auth_code: str):
        pass


def duc_second_auth_service(service_impl: SecondAuthService, session: Session, auth_code: str):
    return service_impl.execute(session, auth_code)


def duc_update_second_auth_code_service(
        service_impl: UpdateSecondAuthService, session: Session, token: str, auth_code: str, new_auth_code: str):
    return service_impl.execute(session, token, auth_code, new_auth_code)

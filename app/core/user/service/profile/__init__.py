from sqlalchemy.orm import Session
from abc import ABC, abstractmethod


class UpdateUserProfile(ABC):

    @abstractmethod
    def execute(self, session: Session,token: str, name: str, email: str, phone_num: str):
        pass


def duc_user_update_profile(service_impl: UpdateUserProfile, session: Session,token: str, name: str, email: str, phone_num: str):
    return service_impl.execute(session, token, name, email, phone_num)

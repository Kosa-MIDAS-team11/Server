from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class CreateDepartmentService(ABC):

    @abstractmethod
    def execute(self, session: Session, token: str, name: str, location: str):
        pass


def duc_create_department(service_impl: CreateDepartmentService, session: Session, token: str, name: str,
                          location: str):
    service_impl.execute(session, token, name, location)

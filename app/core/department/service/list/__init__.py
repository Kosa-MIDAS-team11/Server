from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class DepartmentListService(ABC):

    @abstractmethod
    def execute(self, session, token):
        pass


def duc_query_department_list(service_impi: DepartmentListService, session: Session, token: str):
    return service_impi.execute(session, token)

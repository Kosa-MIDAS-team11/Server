from abc import ABC, abstractmethod


class EmployeeListService(ABC):

    @abstractmethod
    def execute(self, session, token: str, department_id: int):
        pass


def duc_admin_register(service_impl: EmployeeListService,
                       session, token: str, department_id: int):

    return service_impl.execute(session, token, department_id)

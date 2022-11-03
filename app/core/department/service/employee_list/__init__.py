from abc import ABC, abstractmethod


class EmployeeListService(ABC):

    @abstractmethod
    def execute(self, session,token, department_id: str):
        pass


def duc_get_employee_list(service_impl: EmployeeListService, session, token, department_id):
    service_impl.execute(session, token, department_id)

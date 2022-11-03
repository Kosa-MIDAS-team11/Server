from abc import ABC, abstractmethod


class AdminRegisterService(ABC):

    @abstractmethod
    def execute(self, session, department_id: int, email: str, name: str, password: str, phone_num: str,
                is_admin: bool):
        pass


def duc_user_register(service_impl: AdminRegisterService, session,
                      department_id: int, email: str, name: str, password: str, phone_num: str, is_admin: bool):
    return service_impl.execute(session, department_id, email, name, password, phone_num, is_admin)

from abc import ABC, abstractmethod


class AdminRegisterService(ABC):

    @abstractmethod
    def execute(self, session, email: str, name: str, password: str, phone_num: str, is_admin: bool):
        pass


def duc_user_register(service_impl: AdminRegisterService,
                       session, email: str, name: str, password: str, phone_num: str, is_admin: bool):
    return service_impl.execute(session, email, name, password, phone_num, is_admin)

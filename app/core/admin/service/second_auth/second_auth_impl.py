from sqlalchemy.orm import Session

from fastapi import HTTPException, status

from app.core.admin.service.second_auth import SecondAuthService
from app.util.dao.models.code import Code


class SecondAuthServiceImpl(SecondAuthService):

    def execute(self, session: Session, auth_code: str):
        code = session.query(Code).one().auth_code

        if code != auth_code:
            raise HTTPException(400, "인증 코드가 맞지 않습니다!")


second_auth_service_impl = SecondAuthServiceImpl()

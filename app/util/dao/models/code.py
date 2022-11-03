from sqlalchemy import Column, CHAR

from app.util.dao import Base


class Code(Base):

    __tablename__ = 'code'

    auth_code = Column(CHAR(60), primary_key=True)

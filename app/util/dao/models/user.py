from sqlalchemy import Column, BINARY, CHAR, VARCHAR, Boolean

from app.util.dao import Base


class User(Base):

    __tablename__ = 'user'

    email = Column(VARCHAR(50), nullable=False, primary_key=True)
    name = Column(CHAR(5), nullable=False)
    password = Column(CHAR(60), nullable=False)
    phone_num = Column(CHAR(11), nullable=False, unique=True)
    is_admin = Column(Boolean, nullable=False, default=False)



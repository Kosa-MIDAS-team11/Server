from sqlalchemy import Column, BINARY, VARCHAR

from app.util.dao import Base


class Department(Base):

    __tablename__ = 'department'

    department_id = Column(BINARY(16), primary_key=True)
    name = Column(VARCHAR(50), nullable=False, unique=True)
    location = Column(VARCHAR(100), nullable=False)
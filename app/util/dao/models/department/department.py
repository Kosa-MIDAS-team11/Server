from sqlalchemy import Column, INTEGER, VARCHAR

from app.util.dao import Base


class Department(Base):
    __tablename__ = 'department'

    department_id = Column(INTEGER, primary_key=True, autoincrement=True)
    department_name = Column(VARCHAR(50), primary_key=True, nullable=False, unique=True)
    location = Column(VARCHAR(100), nullable=False)

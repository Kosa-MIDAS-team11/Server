from sqlalchemy import ForeignKey, Column, Boolean
from sqlalchemy.orm import relationship

from app.util.dao import Base


class MyDepartment(Base):

    __tablename__ = 'my_department'

    user_email = Column(ForeignKey('user.email'), primary_key=True)
    department_id = Column(ForeignKey('department.department_id'), primary_key=True)
    is_manager = Column(Boolean, nullable=False, default=False)

    user = relationship('User')
    department = relationship('Department')

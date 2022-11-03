from sqlalchemy import Column, ForeignKey, DATE, Boolean
from sqlalchemy.orm import relationship

from app.util.dao import Base


class MyWorkDate(Base):

    __tablename__ = 'my_work_date'

    work_day = Column(DATE, primary_key=True)
    user_id = Column(ForeignKey('user.user_id'), primary_key=True)
    at_home = Column(Boolean, nullable=False, default=False)

    user = relationship('User')